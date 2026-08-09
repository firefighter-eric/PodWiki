from __future__ import annotations

import contextlib
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import qwen3_asr_transformers_adapter as adapter  # noqa: E402


class FakeInferenceMode(contextlib.AbstractContextManager[None]):
    def __enter__(self) -> None:
        return None

    def __exit__(self, *args: object) -> None:
        return None


class FakeTorch:
    def inference_mode(self) -> FakeInferenceMode:
        return FakeInferenceMode()


class FakeInputs(dict[str, object]):
    def __init__(self) -> None:
        super().__init__(input_ids=SimpleNamespace(shape=(1, 3)), feature="audio")
        self.moves: list[tuple[object, object]] = []

    def to(self, device: object, dtype: object) -> "FakeInputs":
        self.moves.append((device, dtype))
        return self


class FakeGeneratedIds:
    def __init__(self) -> None:
        self.slices: list[object] = []

    def __getitem__(self, key: object) -> str:
        self.slices.append(key)
        return "generated-suffix"


class NativeAdapterTests(unittest.TestCase):
    def test_transcription_uses_native_processor_generate_and_suffix_decode(self) -> None:
        calls: list[tuple[str, object]] = []
        inputs = FakeInputs()
        generated = FakeGeneratedIds()

        class Processor:
            def apply_transcription_request(self, **kwargs: object) -> FakeInputs:
                calls.append(("prepare", kwargs))
                return inputs

            def decode(self, ids: object, **kwargs: object) -> list[str]:
                calls.append(("decode", (ids, kwargs)))
                return ["测试文本"]

        class Model:
            device = "cuda:0"
            dtype = "bfloat16"

            def generate(self, **kwargs: object) -> FakeGeneratedIds:
                calls.append(("generate", kwargs))
                return generated

        native = adapter.NativeASR(
            processor=Processor(),
            model=Model(),
            torch=FakeTorch(),
        )

        audio = object()
        self.assertEqual(
            native.transcribe(
                audio=audio,
                language="Chinese",
                max_new_tokens=2048,
            ),
            "测试文本",
        )
        self.assertEqual(calls[0], ("prepare", {"audio": audio, "language": "Chinese"}))
        generate_kwargs = dict(calls[1][1])
        self.assertEqual(generate_kwargs["max_new_tokens"], 2048)
        self.assertIs(generate_kwargs["do_sample"], False)
        self.assertEqual(inputs.moves, [("cuda:0", "bfloat16")])
        self.assertEqual(generated.slices, [(slice(None), slice(3, None))])
        self.assertEqual(
            calls[2],
            (
                "decode",
                (
                    "generated-suffix",
                    {"return_format": "transcription_only"},
                ),
            ),
        )

    def test_forced_alignment_uses_native_prepare_forward_and_decode(self) -> None:
        calls: list[tuple[str, object]] = []
        inputs = FakeInputs()
        decoded = [{"text": "测", "start_time": 0.08, "end_time": 0.16}]

        class Processor:
            def prepare_forced_aligner_inputs(
                self, **kwargs: object
            ) -> tuple[FakeInputs, list[list[str]]]:
                calls.append(("prepare", kwargs))
                return inputs, [["测"]]

            def decode_forced_alignment(self, **kwargs: object) -> list[list[dict[str, object]]]:
                calls.append(("decode", kwargs))
                return [decoded]

        class Model:
            device = "cuda:0"
            dtype = "bfloat16"
            config = SimpleNamespace(timestamp_token_id=42)

            def __call__(self, **kwargs: object) -> SimpleNamespace:
                calls.append(("forward", kwargs))
                return SimpleNamespace(logits="logits")

        native = adapter.NativeForcedAligner(
            processor=Processor(),
            model=Model(),
            torch=FakeTorch(),
        )
        audio = object()

        self.assertEqual(
            native.align(audio=audio, text="测试", language="Chinese"),
            decoded,
        )
        self.assertEqual(
            calls[0],
            (
                "prepare",
                {"audio": audio, "transcript": "测试", "language": "Chinese"},
            ),
        )
        self.assertEqual(inputs.moves, [("cuda:0", "bfloat16")])
        self.assertEqual(
            calls[2],
            (
                "decode",
                {
                    "logits": "logits",
                    "input_ids": inputs["input_ids"],
                    "word_lists": [["测"]],
                    "timestamp_token_id": 42,
                },
            ),
        )

    def test_runtime_loaders_force_local_files_and_eval(self) -> None:
        calls: list[tuple[str, object]] = []

        class ProcessorFactory:
            @staticmethod
            def from_pretrained(target: str, **kwargs: object) -> object:
                calls.append(("processor", (target, kwargs)))
                return object()

        class FakeModel:
            def eval(self) -> None:
                calls.append(("eval", self))

        class ModelFactory:
            @staticmethod
            def from_pretrained(target: str, **kwargs: object) -> FakeModel:
                calls.append(("model", (target, kwargs)))
                return FakeModel()

        runtime = adapter.TransformersNativeRuntime(
            numpy=object(),
            torch=FakeTorch(),
            auto_processor=ProcessorFactory,
            auto_multimodal_model=ModelFactory,
            auto_token_classification_model=ModelFactory,
        )
        runtime.load_asr("C:/model", dtype="bf16", device_map="cuda:0")
        runtime.load_aligner("C:/aligner", dtype="bf16", device_map="cuda:0")

        load_calls = [value for name, value in calls if name in {"processor", "model"}]
        self.assertEqual(len(load_calls), 4)
        for _target, kwargs in load_calls:
            self.assertIs(kwargs["local_files_only"], True)
        model_kwargs = [value[1] for name, value in calls if name == "model"]
        self.assertTrue(all(kwargs["device_map"] == "cuda:0" for kwargs in model_kwargs))
        self.assertEqual(sum(name == "eval" for name, _ in calls), 2)

    def test_versions_and_native_pins_fail_closed(self) -> None:
        adapter.validate_runtime_versions(
            transformers_version="5.14.1",
            torch_version="2.13.0+cu126",
        )
        with self.assertRaisesRegex(SystemExit, "unsupported Transformers"):
            adapter.validate_runtime_versions(
                transformers_version="5.13.0",
                torch_version="2.13.0",
            )
        self.assertEqual(
            adapter.pinned_native_revision(adapter.DEFAULT_MODEL, None),
            adapter.DEFAULT_MODEL_REVISION,
        )
        self.assertEqual(
            adapter.pinned_native_revision(
                adapter.DEFAULT_MODEL,
                adapter.DEFAULT_MODEL_REVISION,
            ),
            adapter.DEFAULT_MODEL_REVISION,
        )
        with self.assertRaisesRegex(ValueError, "unsupported native Qwen repository"):
            adapter.pinned_native_revision("Qwen/custom", "c" * 40)
        with self.assertRaisesRegex(ValueError, "must match the reviewed commit"):
            adapter.pinned_native_revision(adapter.DEFAULT_MODEL, "c" * 40)

    def test_runtime_requires_both_offline_guards_before_import(self) -> None:
        with (
            patch.dict(adapter.os.environ, {}, clear=True),
            patch.object(adapter, "version", side_effect=AssertionError("must not import")),
            self.assertRaisesRegex(RuntimeError, "HF_HUB_OFFLINE"),
        ):
            adapter.load_transformers_native_runtime()


if __name__ == "__main__":
    unittest.main()
