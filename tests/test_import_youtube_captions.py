from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import import_youtube_captions as importer  # noqa: E402
from import_youtube_captions import (  # noqa: E402
    build_outputs,
    caption_segments,
    load_cached_inputs,
    local_translation_segments,
    transcript_bytes,
)


def caption_payload(first: str, second: str, *, shifted: bool = False) -> bytes:
    return json.dumps(
        {
            "wireMagic": "pb3",
            "events": [
                {
                    "tStartMs": 80,
                    "dDurationMs": 3600,
                    "segs": [{"utf8": first}],
                },
                {
                    "tStartMs": 3681 if shifted else 3680,
                    "dDurationMs": 3840,
                    "segs": [{"utf8": second}],
                },
            ],
        },
        ensure_ascii=False,
    ).encode("utf-8")


class YoutubeCaptionImportTests(unittest.TestCase):
    def local_translation_fixture(self):
        source = caption_payload("Hello world", "Second segment")
        segments = caption_segments(json.loads(source), label="source")
        english = transcript_bytes("An episode", segments)
        document = {
            "schema_version": 1, "kind": "podwiki-segment-translation",
            "language": "zh-CN", "source_language": "en", "status": "machine",
            "engine": "mlx-lm", "model": "example/translation-model",
            "model_revision": "a" * 40, "generated_at": "2026-09-25T00:00:00Z",
            "source_payload_sha256": hashlib.sha256(source).hexdigest(),
            "source_transcript_sha256": hashlib.sha256(english).hexdigest(),
            "segments": [{**segment, "text": text} for segment, text in zip(segments, ("你好世界", "第二段"))],
        }
        return source, segments, english, document

    def test_local_translation_preserves_publisher_and_identifies_its_actual_source(self):
        source, segments, english, document = self.local_translation_fixture()
        raw, refined, rendered_en, rendered_zh = build_outputs(
            canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            info={"id": "-RXD4bTuFTo", "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA"},
            source_payload_bytes=source,
            translation_payload_bytes=json.dumps(document, ensure_ascii=False).encode(),
            title="An episode", generated_at="2026-08-18T00:00:00Z",
            source_language="en", translation_track="zh-Hans-en",
            raw_repository_path="raw.json", transcript_repository_path="transcript.en.md",
            translation_repository_path="shows/example/episodes/example/transcript.zh-CN.md",
            local_translation=True,
        )
        self.assertEqual(rendered_en, english)
        self.assertEqual(json.loads(raw)["payload"], json.loads(source))
        self.assertIn("你好世界", rendered_zh.decode())
        provenance = json.loads(refined)["translation"]
        self.assertEqual(provenance["track_type"], "local-machine-translation")
        self.assertNotIn("source_track", provenance)
        self.assertEqual(provenance["model_revision"], "a" * 40)
        self.assertEqual(provenance["source_transcript_sha256"], hashlib.sha256(english).hexdigest())
        self.assertTrue(provenance["payload_path"].endswith("/translation.zh-CN.json"))

    def test_local_translation_rejects_wrong_source_incomplete_or_untraceable_output(self):
        mutations = (
            lambda d: d.update(source_payload_sha256="0" * 64),
            lambda d: d.update(source_transcript_sha256="0" * 64),
            lambda d: d.update(model_revision="main"),
            lambda d: d.update(model_revision=None),
            lambda d: d.update(model_revision=123),
            lambda d: d.update(status="reviewed"),
            lambda d: d.update(generated_at="2026-09-25T00:00:00"),
            lambda d: d.update(segments=d["segments"][:1]),
            lambda d: d["segments"][0].update(text=""),
            lambda d: d["segments"][0].update(text="one\ntwo"),
            lambda d: d["segments"][0].update(start_ms=81),
            lambda d: d["segments"][0].update(source_event_index=False),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                source, segments, english, document = self.local_translation_fixture()
                mutate(document)
                with self.assertRaises(ValueError):
                    local_translation_segments(
                        json.dumps(document).encode(), source_payload=source,
                        source_transcript=english, source_segments=segments,
                    )

    def test_web_translation_records_the_unexposed_model_version_honestly(self):
        source, _, english, document = self.local_translation_fixture()
        document.update(
            engine="google-translate-web", model="Advanced (Gemini)",
            model_revision=None, model_version_visibility="not-exposed",
            provider_url="https://translate.google.com/",
        )
        _, refined, rendered_en, _ = build_outputs(
            canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            info={"id": "-RXD4bTuFTo", "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA"},
            source_payload_bytes=source,
            translation_payload_bytes=json.dumps(document, ensure_ascii=False).encode(),
            title="An episode", generated_at="2026-08-18T00:00:00Z",
            source_language="en", translation_track="zh-Hans-en",
            raw_repository_path="raw.json", transcript_repository_path="transcript.en.md",
            translation_repository_path="shows/example/episodes/example/transcript.zh-CN.md",
            local_translation=True,
        )
        self.assertEqual(rendered_en, english)
        provenance = json.loads(refined)["translation"]
        self.assertEqual(provenance["track_type"], "web-machine-translation")
        self.assertIsNone(provenance["model_revision"])
        self.assertEqual(provenance["model_version_visibility"], "not-exposed")
        self.assertEqual(provenance["provider_url"], "https://translate.google.com/")
        self.assertNotIn("source_track", provenance)

    def test_web_translation_rejects_missing_or_fabricated_provider_identity(self):
        mutations = (
            lambda d: d.pop("model_revision"),
            lambda d: d.update(model_revision="a" * 40),
            lambda d: d.pop("model_version_visibility"),
            lambda d: d.update(model_version_visibility="pinned"),
            lambda d: d.update(model="Unknown model"),
            lambda d: d.update(provider_url="https://example.com/"),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                source, segments, english, document = self.local_translation_fixture()
                document.update(
                    engine="google-translate-web", model="Advanced (Gemini)",
                    model_revision=None, model_version_visibility="not-exposed",
                    provider_url="https://translate.google.com/",
                )
                mutate(document)
                with self.assertRaises(ValueError):
                    local_translation_segments(
                        json.dumps(document).encode(), source_payload=source,
                        source_transcript=english, source_segments=segments,
                    )

    def test_translation_replacement_changes_only_translation_and_provenance(self):
        source, _, english, document = self.local_translation_fixture()
        (ROOT / ".cache").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".cache") as directory:
            root = Path(directory)
            cache = root / ".cache"
            cache.mkdir()
            metadata = cache / "metadata.json"
            metadata.write_text(json.dumps({"source": {
                "platform": "youtube", "id": "-RXD4bTuFTo", "title": "An episode",
                "canonical_url": "https://www.youtube.com/watch?v=-RXD4bTuFTo",
                "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                "availability": "public", "live_status": "not_live",
            }}))
            source_path = cache / "source.json3"
            source_path.write_bytes(source)
            platform_translation = cache / "translation.json3"
            platform_translation.write_bytes(caption_payload("旧译一", "旧译二"))
            local_translation = cache / "translation.json"
            local_translation.write_text(json.dumps(document, ensure_ascii=False))
            episode = root / "shows/example/episodes/example"
            args = argparse.Namespace(
                url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                episode_dir=episode, title=None, run_id="youtube-subtitles",
                source_language="en", translation_track="zh-Hans-en",
                metadata_json=metadata, source_json3=source_path,
                translation_json3=platform_translation, translation_segments_json=None,
                overwrite=False, replace_translation=False, verbose=False,
            )
            with patch.object(importer, "ROOT", root), patch.object(
                importer, "parse_args", return_value=args,
            ), patch.object(importer, "utc_now", return_value="2026-08-18T00:00:00Z"), redirect_stdout(io.StringIO()):
                self.assertEqual(importer.main(), 0)
            before = {p.relative_to(episode): p.read_bytes() for p in episode.rglob("*") if p.is_file()}
            args.translation_json3 = None
            args.translation_segments_json = local_translation
            args.replace_translation = True
            with patch.object(importer, "ROOT", root), patch.object(
                importer, "parse_args", return_value=args,
            ), redirect_stdout(io.StringIO()):
                self.assertEqual(importer.main(), 0)
                for name in (
                    "asr/youtube-subtitles/raw.json", "asr/youtube-subtitles/transcript.en.md",
                    "transcript.en.md",
                ):
                    self.assertEqual((episode / name).read_bytes(), before[Path(name)])
                self.assertEqual((episode / "transcript.en.md").read_bytes(), english)
                self.assertIn("你好世界", (episode / "transcript.zh-CN.md").read_text())
                self.assertEqual((episode / "translation.zh-CN.json").read_bytes(), local_translation.read_bytes())
                refined = json.loads((episode / "asr/youtube-subtitles/refined.json").read_bytes())
                self.assertEqual(refined["translation"]["track_type"], "local-machine-translation")
                self.assertEqual(refined["translation"]["generated_at"], document["generated_at"])

                # A manually changed selected source blocks replacement before any output changes.
                (episode / "transcript.en.md").write_bytes(english + b"manual edit\n")
                protected = {p: p.read_bytes() for p in episode.rglob("*") if p.is_file()}
                with self.assertRaisesRegex(ValueError, "would change the publisher source"):
                    importer.main()
                self.assertEqual({p: p.read_bytes() for p in episode.rglob("*") if p.is_file()}, protected)

                # A conflicting destination also blocks a fresh import before earlier files are written.
                other_episode = root / "shows/example/episodes/another"
                other_episode.mkdir(parents=True)
                conflict = other_episode / "transcript.en.md"
                conflict.write_text("existing user content")
                args.episode_dir = other_episode
                args.replace_translation = False
                with self.assertRaises(FileExistsError):
                    importer.main()
                self.assertFalse((other_episode / "asr").exists())
                self.assertEqual(conflict.read_text(), "existing user content")

    def test_invalid_replacement_never_downloads_or_overwrites(self):
        for local, overwrite in ((None, False), (Path("unused"), True)):
            with self.subTest(local=local, overwrite=overwrite):
                args = argparse.Namespace(
                    url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                    episode_dir=ROOT / "shows/example/episodes/example",
                    translation_segments_json=local, replace_translation=True,
                    overwrite=overwrite,
                )
                with patch.object(importer, "parse_args", return_value=args), patch.object(
                    importer, "download_caption_payloads",
                ) as download:
                    with self.assertRaisesRegex(ValueError, "requires cached segments"):
                        importer.main()
                    download.assert_not_called()

    def test_resumes_only_from_source_bound_cache_inputs(self) -> None:
        cache_root = ROOT / ".cache"
        cache_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache_root) as directory:
            input_dir = Path(directory)
            metadata_path = input_dir / "source.metadata.json"
            source_path = input_dir / "subtitle.en.json3"
            translation_path = input_dir / "subtitle.zh-Hans-en.json3"
            metadata_path.write_text(
                json.dumps(
                    {
                        "source": {
                            "platform": "youtube",
                            "canonical_url": (
                                "https://www.youtube.com/watch?v=-RXD4bTuFTo"
                            ),
                            "id": "-RXD4bTuFTo",
                            "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                            "availability": "public",
                            "live_status": "not_live",
                        }
                    }
                ),
                encoding="utf-8",
            )
            source_path.write_bytes(caption_payload("One", "Two"))
            translation_path.write_bytes(caption_payload("一", "二"))

            info, source, translation = load_cached_inputs(
                metadata_path=metadata_path,
                source_path=source_path,
                translation_path=translation_path,
                canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            )

            self.assertEqual(info["id"], "-RXD4bTuFTo")
            self.assertEqual(source, source_path.read_bytes())
            self.assertEqual(translation, translation_path.read_bytes())

    def test_rejects_cached_inputs_outside_repository_cache(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "input.json"
            input_path.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "repository .cache"):
                load_cached_inputs(
                    metadata_path=input_path,
                    source_path=input_path,
                    translation_path=input_path,
                    canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                )

    def test_builds_aligned_english_and_chinese_transcripts(self) -> None:
        raw, refined, english, chinese = build_outputs(
            canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
            info={
                "id": "-RXD4bTuFTo",
                "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                "uploader": "Dwarkesh Patel",
            },
            source_payload_bytes=caption_payload("Hello\nworld", "Second  segment"),
            translation_payload_bytes=caption_payload("你好\n世界", "第二段"),
            title="An episode",
            generated_at="2026-08-18T00:00:00Z",
            source_language="en",
            translation_track="zh-Hans-en",
            raw_repository_path="shows/example/episodes/example/asr/youtube-subtitles/raw.json",
            transcript_repository_path=(
                "shows/example/episodes/example/asr/youtube-subtitles/transcript.en.md"
            ),
            translation_repository_path=(
                "shows/example/episodes/example/transcript.zh-CN.md"
            ),
        )

        raw_document = json.loads(raw)
        refined_document = json.loads(refined)
        self.assertEqual(raw_document["source"]["video_id"], "-RXD4bTuFTo")
        self.assertEqual(len(refined_document["segments"]), 2)
        self.assertIn("[00:00:00] Hello world  \n", english.decode("utf-8"))
        self.assertIn("[00:00:00] 你好 世界  \n", chinese.decode("utf-8"))
        self.assertEqual(
            refined_document["translation"]["event_count"],
            len(caption_segments(json.loads(caption_payload("一", "二")), label="test")),
        )

    def test_rejects_translation_timestamp_drift(self) -> None:
        with self.assertRaisesRegex(ValueError, "does not preserve source start_ms"):
            build_outputs(
                canonical_url="https://www.youtube.com/watch?v=-RXD4bTuFTo",
                info={
                    "id": "-RXD4bTuFTo",
                    "channel_id": "UCXl4i9dYBrFOabk0xGmbkRA",
                    "uploader": "Dwarkesh Patel",
                },
                source_payload_bytes=caption_payload("One", "Two"),
                translation_payload_bytes=caption_payload("一", "二", shifted=True),
                title="An episode",
                generated_at="2026-08-18T00:00:00Z",
                source_language="en",
                translation_track="zh-Hans-en",
                raw_repository_path="raw.json",
                transcript_repository_path="transcript.en.md",
                translation_repository_path="transcript.zh-CN.md",
            )


if __name__ == "__main__":
    unittest.main()
