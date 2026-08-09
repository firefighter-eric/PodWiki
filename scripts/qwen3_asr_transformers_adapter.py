#!/usr/bin/env python3
"""Small, strict adapter for Transformers-native Qwen3-ASR inference."""

from __future__ import annotations

import os
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from typing import Any


TRANSFORMERS_PACKAGE_VERSION = "5.14.1"
TORCH_PUBLIC_VERSION = "2.13.0"
DEFAULT_MODEL = "Qwen/Qwen3-ASR-1.7B-hf"
DEFAULT_MODEL_REVISION = "bcd2b5b7f32b480ab5790554cfa8347f246a14f3"
DEFAULT_ALIGNER = "Qwen/Qwen3-ForcedAligner-0.6B-hf"
DEFAULT_ALIGNER_REVISION = "c07281df297b9905d24a508279258cccf987a064"


def pinned_native_revision(repository: str, requested_revision: str | None) -> str:
    """Resolve only the two reviewed native repositories at their reviewed commits."""
    reviewed_revision = {
        DEFAULT_MODEL: DEFAULT_MODEL_REVISION,
        DEFAULT_ALIGNER: DEFAULT_ALIGNER_REVISION,
    }.get(repository)
    if reviewed_revision is None:
        raise ValueError(
            f"unsupported native Qwen repository: {repository!r}; expected "
            f"{DEFAULT_MODEL!r} or {DEFAULT_ALIGNER!r}"
        )
    if requested_revision is None:
        return reviewed_revision
    if len(requested_revision) != 40 or any(
        character not in "0123456789abcdefABCDEF"
        for character in requested_revision
    ):
        raise ValueError(
            f"model revision for {repository!r} must be a full 40-character commit"
        )
    normalized_revision = requested_revision.lower()
    if normalized_revision != reviewed_revision:
        raise ValueError(
            f"model revision for {repository!r} must match the reviewed commit "
            f"{reviewed_revision}"
        )
    return reviewed_revision


def require_offline_mode() -> None:
    """Fail before importing or loading model code unless both offline guards are set."""
    missing = [
        name
        for name in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE")
        if os.environ.get(name) != "1"
    ]
    if missing:
        raise RuntimeError(
            "Transformers-native Qwen requires pinned local snapshots and offline mode; "
            f"set {', '.join(missing)}=1"
        )


def validate_runtime_versions(
    *, transformers_version: str, torch_version: str
) -> None:
    if transformers_version != TRANSFORMERS_PACKAGE_VERSION:
        raise SystemExit(
            "unsupported Transformers package version: "
            f"expected={TRANSFORMERS_PACKAGE_VERSION}, actual={transformers_version}"
        )
    torch_public_version = str(torch_version).partition("+")[0]
    if torch_public_version != TORCH_PUBLIC_VERSION:
        raise SystemExit(
            "unsupported PyTorch package version: "
            f"expected={TORCH_PUBLIC_VERSION}, actual={torch_version}"
        )


@dataclass(frozen=True)
class NativeASR:
    processor: Any
    model: Any
    torch: Any

    def transcribe(
        self,
        *,
        audio: Any,
        language: str,
        max_new_tokens: int,
    ) -> str:
        inputs = self.processor.apply_transcription_request(
            audio=audio,
            language=language,
        )
        inputs = inputs.to(self.model.device, self.model.dtype)
        prompt_tokens = inputs["input_ids"].shape[1]
        with self.torch.inference_mode():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
            )
        generated_ids = output_ids[:, prompt_tokens:]
        decoded = self.processor.decode(
            generated_ids,
            return_format="transcription_only",
        )
        if not isinstance(decoded, list) or len(decoded) != 1:
            raise ValueError("Qwen3-ASR returned an unexpected result count")
        text = decoded[0]
        if not isinstance(text, str):
            raise ValueError("Qwen3-ASR returned no transcript text")
        return text


@dataclass(frozen=True)
class NativeForcedAligner:
    processor: Any
    model: Any
    torch: Any

    def align(self, *, audio: Any, text: str, language: str) -> list[dict[str, Any]]:
        inputs, word_lists = self.processor.prepare_forced_aligner_inputs(
            audio=audio,
            transcript=text,
            language=language,
        )
        inputs = inputs.to(self.model.device, self.model.dtype)
        with self.torch.inference_mode():
            outputs = self.model(**inputs)
        decoded = self.processor.decode_forced_alignment(
            logits=outputs.logits,
            input_ids=inputs["input_ids"],
            word_lists=word_lists,
            timestamp_token_id=self.model.config.timestamp_token_id,
        )
        if not isinstance(decoded, list) or len(decoded) != 1:
            raise ValueError("Qwen3-ForcedAligner returned an unexpected result count")
        items = decoded[0]
        if not isinstance(items, list):
            raise ValueError("Qwen3-ForcedAligner returned a non-list result")
        return items


@dataclass(frozen=True)
class TransformersNativeRuntime:
    numpy: Any
    torch: Any
    auto_processor: Any
    auto_multimodal_model: Any
    auto_token_classification_model: Any

    def load_asr(self, target: str, **model_kwargs: Any) -> NativeASR:
        processor = self.auto_processor.from_pretrained(
            target,
            local_files_only=True,
        )
        model = self.auto_multimodal_model.from_pretrained(
            target,
            local_files_only=True,
            **model_kwargs,
        )
        model.eval()
        return NativeASR(processor=processor, model=model, torch=self.torch)

    def load_aligner(self, target: str, **model_kwargs: Any) -> NativeForcedAligner:
        processor = self.auto_processor.from_pretrained(
            target,
            local_files_only=True,
        )
        model = self.auto_token_classification_model.from_pretrained(
            target,
            local_files_only=True,
            **model_kwargs,
        )
        model.eval()
        return NativeForcedAligner(processor=processor, model=model, torch=self.torch)


def load_transformers_native_runtime() -> TransformersNativeRuntime:
    require_offline_mode()
    try:
        import numpy as np
        import torch
        from transformers import (
            AutoModelForMultimodalLM,
            AutoModelForTokenClassification,
            AutoProcessor,
        )

        transformers_version = version("transformers")
    except (ImportError, PackageNotFoundError) as error:
        raise SystemExit(
            "the Transformers-native CUDA Qwen backend is unavailable; run "
            "`uv sync --locked --extra media --extra asr-cuda`, then use the "
            "dedicated Windows CUDA interpreter for this worker"
        ) from error
    validate_runtime_versions(
        transformers_version=transformers_version,
        torch_version=str(torch.__version__),
    )
    return TransformersNativeRuntime(
        numpy=np,
        torch=torch,
        auto_processor=AutoProcessor,
        auto_multimodal_model=AutoModelForMultimodalLM,
        auto_token_classification_model=AutoModelForTokenClassification,
    )
