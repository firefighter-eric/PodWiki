from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path
from unittest.mock import patch

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import transcribe_qwen3_asr_cuda as worker  # noqa: E402


class AudioDecodeProfileTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg is required for PCM integration")
    def test_normalized_float_downmix_matches_integer_pcm_without_overflow(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "stereo.wav"
            t = np.arange(16000) / 16000
            left = np.rint(0.9 * np.sin(2 * np.pi * 300 * t) * 32767).astype("<i2")
            right = left.copy()
            with wave.open(str(source), "wb") as handle:
                handle.setnchannels(2)
                handle.setsampwidth(2)
                handle.setframerate(16000)
                handle.writeframes(np.column_stack((left, right)).tobytes())
            original_sha = hashlib.sha256(source.read_bytes()).hexdigest()
            legacy = worker.decode_audio_chunk(
                source, start_seconds=0, end_seconds=1, ffmpeg="ffmpeg", numpy_module=np
            )
            token = worker.AUDIO_DECODE_PROFILE.set(worker.NORMALIZED_AUDIO_DECODE_PROFILE)
            try:
                normalized = worker.decode_audio_chunk(
                    source, start_seconds=0, end_seconds=1, ffmpeg="ffmpeg", numpy_module=np
                )
            finally:
                worker.AUDIO_DECODE_PROFILE.reset(token)
            integer_bytes = subprocess.run(
                ["ffmpeg", "-v", "error", "-i", str(source), "-ac", "1", "-ar", "16000",
                 "-f", "s16le", "pipe:1"],
                check=True, capture_output=True,
            ).stdout
            integer_reference = np.frombuffer(integer_bytes, dtype="<i2") / 32768
            self.assertEqual(len(normalized), len(integer_reference))
            np.testing.assert_allclose(normalized, integer_reference, atol=2 / 32768)
            np.testing.assert_allclose(normalized, left / 32768, atol=2 / 32768)
            self.assertGreater(float(np.max(np.abs(legacy))), 1.0)
            self.assertLess(float(np.max(np.abs(normalized))), 1.0)
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), original_sha)

    def test_profile_is_opt_in_and_scoped_even_after_worker_failure(self) -> None:
        self.assertEqual(worker.AUDIO_DECODE_PROFILE.get(), worker.LEGACY_AUDIO_DECODE_PROFILE)
        args = argparse.Namespace(audio_decode_profile=worker.NORMALIZED_AUDIO_DECODE_PROFILE)

        def fail(bound_args: argparse.Namespace) -> int:
            self.assertIs(bound_args, args)
            self.assertEqual(worker.AUDIO_DECODE_PROFILE.get(), args.audio_decode_profile)
            raise RuntimeError("native model failure")

        with patch.object(worker, "parse_args", return_value=args), patch.object(
            worker, "run_worker", side_effect=fail
        ), self.assertRaisesRegex(RuntimeError, "native model failure"):
            worker.main()
        self.assertEqual(worker.AUDIO_DECODE_PROFILE.get(), worker.LEGACY_AUDIO_DECODE_PROFILE)
        self.assertEqual(worker.audio_decode_options(argparse.Namespace()), {})

    def test_aligned_profile_must_match_raw_and_reject_unknown_profiles(self) -> None:
        raw = {"options": {"audio_decode_profile": worker.NORMALIZED_AUDIO_DECODE_PROFILE}}
        aligned = {"options": {}}
        with self.assertRaisesRegex(ValueError, "profile does not match raw"):
            worker.validate_cuda_aligned_integrity(
                aligned, raw_output_path=Path("raw.json"), raw_document=raw
            )
        for invalid in (None, "silence", "normalized-rematrix-v2", False):
            with self.subTest(invalid=invalid), self.assertRaisesRegex(ValueError, "profile"):
                worker.validated_audio_decode_profile(invalid)

    def test_profile_does_not_exempt_active_untranscribed_audio(self) -> None:
        audio = (0.1 * np.sin(2 * np.pi * 300 * np.arange(320000) / 16000)).astype(np.float32)
        chunk = {"start": 0.0, "end": 60.0,
                 "alignment": [{"text": "好", "start": 0.0, "end": 1.0}]}
        token = worker.AUDIO_DECODE_PROFILE.set(worker.NORMALIZED_AUDIO_DECODE_PROFILE)
        try:
            with patch.object(worker, "decode_audio_chunk", return_value=audio), self.assertRaisesRegex(
                ValueError, "active-audio-coverage-v1"
            ):
                worker.enforce_alignment_coverage(
                    input_path=Path("speech.wav"), chunks=[chunk], ffmpeg="ffmpeg", numpy_module=np
                )
        finally:
            worker.AUDIO_DECODE_PROFILE.reset(token)


if __name__ == "__main__":
    unittest.main()
