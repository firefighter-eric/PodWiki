from __future__ import annotations

import argparse
import copy
import contextlib
import hashlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import transcribe_qwen3_asr_cuda as cuda_worker  # noqa: E402
from transcribe_qwen3_asr import (  # noqa: E402
    read_json_strict,
    sha256_file,
    write_json_atomically,
)


class FakeAudio:
    def __init__(self, samples: int = 32_000) -> None:
        self.samples = samples

    def __len__(self) -> int:
        return self.samples


class FakeCuda:
    def __init__(self) -> None:
        self.current_device = 0

    def is_available(self) -> bool:
        return True

    def device_count(self) -> int:
        return 1

    def is_bf16_supported(self) -> bool:
        return True

    def set_device(self, index: int) -> None:
        self.current_device = index

    def get_device_properties(self, index: int) -> SimpleNamespace:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")
        return SimpleNamespace(name="Fake RTX", total_memory=8 * 1024**3)

    def reset_peak_memory_stats(self, index: int) -> None:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")

    def synchronize(self, index: int) -> None:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")

    def max_memory_allocated(self, index: int) -> int:
        if index != 0:
            raise AssertionError(f"unexpected device index: {index}")
        return 512 * 1024**2

    def empty_cache(self) -> None:
        return None


class FakeTorch:
    def __init__(self) -> None:
        self.cuda = FakeCuda()
        self.version = SimpleNamespace(cuda="12.8")
        self.float16 = object()
        self.bfloat16 = object()


class WorkerHarness:
    def __init__(self) -> None:
        self.events: list[tuple[str, object]] = []
        self.torch = FakeTorch()
        events = self.events

        class FakeASRModel:
            @classmethod
            def from_pretrained(cls, target: str, **kwargs: object) -> "FakeASRModel":
                events.append(("load-asr", (target, kwargs)))
                return cls()

            def transcribe(self, **kwargs: object) -> list[SimpleNamespace]:
                events.append(("transcribe", kwargs))
                return [SimpleNamespace(text="Test.")]

        class FakeAligner:
            @classmethod
            def from_pretrained(cls, target: str, **kwargs: object) -> "FakeAligner":
                events.append(("load-aligner", (target, kwargs)))
                return cls()

            def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                events.append(("align", kwargs))
                return [
                    [
                        SimpleNamespace(
                            text="Test",
                            start_time=0.1,
                            end_time=1.5,
                        )
                    ]
                ]

        self.asr_model = FakeASRModel
        self.aligner = FakeAligner

    def runtime(self) -> tuple[object, FakeTorch, type[object], type[object]]:
        return object(), self.torch, self.asr_model, self.aligner


def write_fake_model_snapshot(path: Path, *, repository: str) -> None:
    path.mkdir(parents=True, exist_ok=True)
    payloads = {
        "config.json": b"{}\n",
        "model.safetensors": b"test model weights",
    }
    for logical_name, payload in payloads.items():
        (path / logical_name).write_bytes(payload)
    metadata = path / ".cache" / "huggingface" / "download"
    metadata.mkdir(parents=True, exist_ok=True)
    for logical_name, payload in payloads.items():
        (metadata / f"{logical_name}.metadata").write_text(
            f"{cuda_worker.pinned_revision(repository, None)}\n"
            f"{hashlib.sha256(payload).hexdigest()}\n0\n",
            encoding="utf-8",
        )


def worker_args(directory: Path) -> argparse.Namespace:
    model_path = directory / "model" if directory.is_dir() else None
    aligner_path = directory / "aligner" if directory.is_dir() else None
    if model_path is not None and aligner_path is not None:
        write_fake_model_snapshot(model_path, repository=cuda_worker.DEFAULT_MODEL)
        write_fake_model_snapshot(aligner_path, repository=cuda_worker.DEFAULT_ALIGNER)
    return argparse.Namespace(
        input=directory / "source.m4a",
        output=directory / "raw.json",
        aligned_output=directory / "aligned.json",
        model=cuda_worker.DEFAULT_MODEL,
        model_path=model_path,
        model_revision=None,
        aligner=cuda_worker.DEFAULT_ALIGNER,
        aligner_path=aligner_path,
        aligner_revision=None,
        language="English",
        temperature=0.0,
        max_tokens=2048,
        chunk_duration=120.0,
        chunk_context=5.0,
        final_outro_exemption_seconds=0.0,
        max_sentence_characters=160,
        device="cuda:0",
        dtype="float16",
        attention_implementation="sdpa",
        verbose=False,
        retranscribe=False,
        realign=False,
    )


def alignment_items_at_midpoints(
    text: str,
    midpoints: list[float],
) -> list[dict[str, object]]:
    return [
        {
            "text": character,
            "start": midpoint - 0.02,
            "end": midpoint + 0.02,
        }
        for character, midpoint in zip(text, midpoints, strict=True)
    ]


def observed_right_extra_indel_items(
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    left_text = "虽然我我这几天一直在遇到很多"
    right_text = "虽然我我我这几天一直在遇到很多"
    left_midpoints = [
        1259.48,
        1259.60,
        1259.80,
        1260.28,
        1260.60,
        1260.88,
        1261.16,
        1261.32,
        1261.48,
        1261.72,
        1261.88,
        1262.16,
        1262.72,
        1262.88,
    ]
    right_midpoints = [
        1259.44,
        1259.60,
        1259.80,
        1260.28,
        1260.44,
        1260.64,
        1260.88,
        1261.16,
        1261.32,
        1261.48,
        1261.72,
        1261.88,
        1262.16,
        1262.72,
        1262.88,
    ]
    return (
        alignment_items_at_midpoints(left_text, left_midpoints),
        alignment_items_at_midpoints(right_text, right_midpoints),
    )


def observed_right_extra_indel_runs(
    left_items: list[dict[str, object]],
    right_items: list[dict[str, object]],
    *,
    earlier_run: list[tuple[int, int]] | None = None,
    later_run: list[tuple[int, int]] | None = None,
) -> list[tuple[list[tuple[int, int]], int, float]]:
    left_overlap = list(enumerate(left_items))
    right_overlap = list(enumerate(right_items))
    runs = [
        earlier_run or [(index, index) for index in range(4)],
        later_run or [(2 + index, 3 + index) for index in range(12)],
    ]
    return [
        (
            run,
            cuda_worker._match_run_characters(run, left_overlap),
            cuda_worker._match_run_max_pair_delta(
                run,
                left_overlap,
                right_overlap,
            ),
        )
        for run in runs
    ]


def observed_zero_duration_right_indel_bridge_items(
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Return the real episode-18 seam-480 candidate shape and indices."""

    earlier_text = "因为刚才会长也问了一个问题说他很也说"
    later_text = "他很喜欢就是我很好奇啊这个从我认识"
    left_midpoints = [
        477.16,
        477.24,
        477.40,
        477.52,
        477.64,
        477.80,
        477.92,
        478.04,
        478.20,
        478.28,
        478.40,
        478.48,
        478.60,
        478.80,
        479.24,
        479.36,
        479.56,
        479.76,
        479.92,
        480.04,
        480.20,
        480.36,
        480.56,
        480.64,
        480.80,
        481.00,
        481.20,
        481.40,
        481.52,
        481.60,
        481.68,
        482.12,
        482.32,
        482.48,
        482.76,
    ]
    right_midpoints = [
        477.16,
        477.28,
        477.40,
        477.52,
        477.64,
        477.80,
        477.92,
        478.04,
        478.20,
        478.28,
        478.40,
        478.48,
        478.60,
        478.80,
        479.24,
        479.36,
        479.56,
        479.76,
        479.88,
        479.92,
        480.04,
        480.20,
        480.36,
        480.56,
        480.64,
        480.80,
        481.00,
        481.20,
        481.40,
        481.52,
        481.60,
        481.68,
        482.12,
        482.32,
        482.48,
        482.80,
    ]
    left_core = alignment_items_at_midpoints(
        earlier_text + later_text,
        left_midpoints,
    )
    right_core = alignment_items_at_midpoints(
        earlier_text + "了" + later_text,
        right_midpoints,
    )
    left_core[17] = {"text": "说", "start": 479.64, "end": 479.88}
    left_core[18] = {"text": "他", "start": 479.88, "end": 479.96}
    right_core[17] = {"text": "说", "start": 479.64, "end": 479.88}
    right_core[18] = {"text": "了", "start": 479.88, "end": 479.88}
    right_core[19] = {"text": "他", "start": 479.88, "end": 479.96}
    left_prefix = [
            {"text": "左", "start": 470.0, "end": 470.001}
            for _ in range(319)
        ]
    left_prefix[-2] = {"text": "么", "start": 476.76, "end": 476.84}
    left_prefix[-1] = {"text": "快", "start": 476.92, "end": 477.08}
    right_prefix = [
            {"text": "右", "start": 470.0, "end": 470.001}
            for _ in range(12)
        ]
    right_prefix[-1] = {"text": "快", "start": 476.84, "end": 477.08}
    suffix = {"text": "知", "start": 483.16, "end": 483.32}
    return (
        left_prefix + left_core + [copy.deepcopy(suffix)],
        right_prefix + right_core + [copy.deepcopy(suffix)],
    )


def observed_single_axis_weak_run_items(
    case: str,
) -> tuple[
    list[dict[str, object]],
    list[dict[str, object]],
    float,
    tuple[int, int],
]:
    """Return compact midpoint-exact fixtures for the four observed seams."""

    fixtures = {
        "5": (
            1560.0,
            627,
            "里算不算敏感但对我来说不算敏感我是八月底到期的嘛八月底到期然后他有三个月的你不能",
            [-2.96, -2.84, -2.72, -2.64, -2.52, -2.36, -2.2, -2.04, -1.92, -1.84, -1.72, -1.6, -1.48, -1.36, -1.24, -0.84, -0.8, -0.68, -0.52, -0.36, -0.2, 0.0, 0.16, 0.24, 0.44, 0.52, 0.52, 0.77, 0.81, 0.88, 0.96, 1.04, 1.12, 1.28, 1.48, 1.64, 1.8, 2.36, 2.56, 2.8],
            15,
            "里算不算敏感但对我来说不算敏感我是八月底到的嘛八月底到既然他有三个月的你不能",
            [-2.96, -2.84, -2.72, -2.64, -2.52, -2.36, -2.2, -2.04, -1.92, -1.84, -1.72, -1.6, -1.52, -1.36, -1.24, -0.88, -0.8, -0.68, -0.52, -0.36, -0.2, -0.08, 0.2, 0.36, 0.48, 0.56, 0.64, 0.76, 0.92, 1.04, 1.12, 1.28, 1.48, 1.64, 1.8, 2.36, 2.56, 2.8],
            (649, 36),
        ),
        "12": (
            6000.0,
            648,
            "你还要在在后面你要把一些该拿的成就你还成绩你还要拿下来我觉得同样吧这件事情同",
            [-2.92, -2.76, -2.64, -2.4, -1.96, -1.8, -1.64, -1.52, -1.4, -1.24, -1.12, -1.04, -0.88, -0.72, -0.64, -0.52, -0.36, -0.24, -0.16, 0.0, 0.16, 0.24, 0.36, 0.48, 0.64, 0.76, 0.96, 1.24, 1.4, 1.64, 1.96, 2.12, 2.24, 2.32, 2.44, 2.6, 2.76, 2.92],
            11,
            "你还要在在后面你要把一些该拿的成绩你成绩你还要拿下来我觉得同样吧这件事情同样",
            [-2.92, -2.76, -2.64, -2.48, -1.96, -1.8, -1.68, -1.52, -1.4, -1.24, -1.16, -1.08, -0.92, -0.72, -0.64, -0.52, -0.4, -0.24, 0.0, 0.12, 0.24, 0.36, 0.48, 0.64, 0.76, 0.96, 1.24, 1.4, 1.52, 1.96, 2.12, 2.24, 2.32, 2.44, 2.6, 2.72, 2.88, 3.0],
            (668, 30),
        ),
        "13": (
            2160.0,
            552,
            "嗯前两年年赞助费没那么多是吧没那么那退费呢退费拿到了吗没有啊",
            [-2.68, -2.28, -2.16, -2.04, -1.6, -0.96, -0.88, -0.8, -0.68, -0.56, -0.52, -0.36, -0.24, -0.16, 0.12, 0.32, 0.4, 0.72, 1.2, 1.4, 1.52, 1.64, 1.84, 1.96, 2.08, 2.12, 2.24, 2.56, 2.72, 2.8],
            9,
            "嗯前两年赞助费没那么多是吧没那么多那退费呢退费拿到了吗没有啊",
            [-2.64, -2.28, -2.16, -2.04, -0.96, -0.88, -0.8, -0.68, -0.56, -0.48, -0.36, -0.24, -0.16, 0.12, 0.32, 0.4, 0.48, 0.76, 1.2, 1.36, 1.48, 1.64, 1.8, 1.96, 2.08, 2.16, 2.24, 2.56, 2.72, 2.8],
            (566, 22),
        ),
        "14": (
            5400.0,
            513,
            "比如说情绪比较低落的低落的时候他会安慰我然后呢在我身",
            [-2.44, -2.32, -2.04, -1.6, -1.4, -1.28, -1.16, -0.92, -0.76, -0.64, -0.12, 0.04, 0.16, 0.36, 0.64, 0.92, 1.04, 1.24, 1.44, 1.6, 2.16, 2.36, 2.52, 2.68, 2.84, 3.0],
            6,
            "比如说情绪比较低落的时低落的时候他会安慰我然后呢在我身",
            [-2.48, -2.36, -2.12, -1.6, -1.4, -1.28, -1.16, -0.92, -0.76, -0.64, -0.52, -0.12, 0.04, 0.16, 0.36, 0.64, 0.92, 1.04, 1.24, 1.4, 1.68, 2.16, 2.36, 2.52, 2.68, 2.84, 3.0],
            (524, 18),
        ),
    }
    (
        seam,
        left_start,
        left_text,
        left_offsets,
        right_start,
        right_text,
        right_offsets,
        cut,
    ) = fixtures[case]

    def side_items(
        start_index: int, text: str, offsets: list[float]
    ) -> list[dict[str, object]]:
        prefix = [
            {"text": "前", "start": seam - 5.0, "end": seam - 4.999}
            for _ in range(start_index)
        ]
        prefix[-1] = {
            "text": "界",
            "start": seam - 3.22,
            "end": seam - 3.18,
        }
        candidate = alignment_items_at_midpoints(
            text, [seam + offset for offset in offsets]
        )
        return prefix + candidate + [
            {"text": "界", "start": seam + 3.18, "end": seam + 3.22}
        ]

    return (
        side_items(left_start, left_text, left_offsets),
        side_items(right_start, right_text, right_offsets),
        seam,
        cut,
    )


def left_exhausted_seam_items(
    *,
    terminal_midpoint: float = 96.0,
    edge_text: str = "甲乙丙",
    edge_delta: float = 0.04,
    tail_text: str = "",
    handoff_gap: float = 0.28,
    right_crosses_seam: bool = True,
    crossing_start: float = 119.8,
    crossing_end: float = 120.2,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    last_anchor_midpoint = terminal_midpoint - 0.75 * len(tail_text)
    first_anchor_midpoint = last_anchor_midpoint - 0.5 * (len(edge_text) - 1)
    prefix_count = 36 - len(edge_text) - len(tail_text)
    prefix_stop = first_anchor_midpoint - 1.0
    prefix_step = (prefix_stop - 61.0) / max(1, prefix_count - 1)
    prefix_midpoints = [61.0 + prefix_step * index for index in range(prefix_count)]
    anchor_midpoints = [
        first_anchor_midpoint + 0.5 * index for index in range(len(edge_text))
    ]
    tail_midpoints = [
        last_anchor_midpoint + 0.75 * (index + 1)
        for index in range(len(tail_text))
    ]
    left_items = alignment_items_at_midpoints(
        "".join(chr(0x6000 + index) for index in range(prefix_count))
        + edge_text
        + tail_text,
        [*prefix_midpoints, *anchor_midpoints, *tail_midpoints],
    )
    right_items = alignment_items_at_midpoints(
        edge_text,
        [midpoint + edge_delta for midpoint in anchor_midpoints],
    )

    next_text = 0x7000
    bridge_start = float(left_items[prefix_count + len(edge_text) - 1]["end"])
    bridge_start += handoff_gap
    while bridge_start + 0.04 < 119.8:
        right_items.append(
            {
                "text": chr(next_text),
                "start": bridge_start,
                "end": bridge_start + 0.04,
            }
        )
        next_text += 1
        bridge_start += 0.5
    if right_crosses_seam:
        right_items.append(
            {
                "text": chr(next_text),
                "start": crossing_start,
                "end": crossing_end,
            }
        )
        next_text += 1
    else:
        right_items.extend(
            [
                {"text": chr(next_text), "start": 119.8, "end": 120.0},
                {"text": chr(next_text + 1), "start": 120.0, "end": 120.2},
            ]
        )
        next_text += 2
    for midpoint in (120.5, 121.0, 121.5, 122.0, 122.5, 123.0):
        right_items.append(
            {
                "text": chr(next_text),
                "start": midpoint - 0.02,
                "end": midpoint + 0.02,
            }
        )
        next_text += 1
    return left_items, right_items


def shifted_alignment_items(
    items: list[dict[str, object]],
    offset_seconds: float,
) -> list[dict[str, object]]:
    return [
        {
            **item,
            "start": float(item["start"]) + offset_seconds,
            "end": float(item["end"]) + offset_seconds,
        }
        for item in items
    ]


def completed_two_chunk_raw_fixture(
    *,
    chunk_context: float,
    left_items: list[dict[str, object]],
    right_items: list[dict[str, object]],
    left_stop: int,
    right_start: int,
    seam_record: dict[str, object],
) -> tuple[argparse.Namespace, dict[str, object], dict[str, object]]:
    args = worker_args(Path("fixture"))
    args.language = "Chinese"
    args.chunk_context = chunk_context
    backend_options = cuda_worker.raw_backend_options(args)
    windows = list(
        cuda_worker.audio_chunk_ranges(
            240.0,
            chunk_duration=args.chunk_duration,
            chunk_context=args.chunk_context,
        )
    )
    item_sets = (left_items, right_items)
    ownership_slices = ((0, left_stop), (right_start, len(right_items)))
    segments: list[dict[str, object]] = []
    for index, (window, items, ownership) in enumerate(
        zip(windows, item_sets, ownership_slices, strict=True)
    ):
        decoded_text = "".join(str(item["text"]) for item in items)
        owned_start, owned_stop = ownership
        segments.append(
            {
                "id": index,
                "start": cuda_worker.rounded_seconds(window.ownership_start),
                "end": cuda_worker.rounded_seconds(window.ownership_end),
                "decode_start": cuda_worker.rounded_seconds(window.decode_start),
                "decode_end": cuda_worker.rounded_seconds(window.decode_end),
                "decoded_text": decoded_text,
                "text": "".join(
                    str(item["text"])
                    for item in items[owned_start:owned_stop]
                ),
                "owned_item_start": owned_start,
                "owned_item_stop": owned_stop,
            }
        )
    seam = {
        "left_chunk_id": 0,
        "right_chunk_id": 1,
        **copy.deepcopy(seam_record),
    }
    document: dict[str, object] = {
        "audio": {
            "sample_rate_hz": cuda_worker.SAMPLE_RATE,
            "duration_seconds": 240.0,
        },
        "options": {
            "temperature": args.temperature,
            "max_tokens_per_chunk": args.max_tokens,
            "chunk_duration_seconds": args.chunk_duration,
            "chunk_context_seconds": args.chunk_context,
            "boundary_reconciliation": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
            "alignment_coverage_guard": cuda_worker.ALIGNMENT_COVERAGE_GUARD,
            "aligned_gap_guard": cuda_worker.ALIGNED_GAP_GUARD,
            **backend_options,
        },
        "boundary_reconciliation": {
            "method": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
            "status": "complete",
            "chunk_context_seconds": args.chunk_context,
            "seams": [seam],
        },
        "text": cuda_worker.join_transcript_chunks(
            [str(segment["text"]) for segment in segments],
            language=args.language,
        ),
        "segments": segments,
    }
    return args, backend_options, document


def completed_exhausted_fixture(
    *,
    edge_delta: float = 0.04,
    crossing_start: float = 119.8,
    crossing_end: float = 120.2,
) -> tuple[
    argparse.Namespace,
    dict[str, object],
    dict[str, object],
    list[dict[str, object]],
    list[dict[str, object]],
]:
    left_items, right_items = left_exhausted_seam_items(
        edge_delta=edge_delta,
        crossing_start=crossing_start,
        crossing_end=crossing_end,
    )
    # Keep the synthetic first 120-second ownership dense enough that the
    # exhausted frontier is its only coverage suspicion. The seam proof itself
    # remains entirely inside the shared 90-150 second decode window.
    left_items = alignment_items_at_midpoints(
        "".join(chr(0x5800 + index) for index in range(30)),
        [0.5 + 2.0 * index for index in range(30)],
    ) + left_items
    left_stop, right_start, record = cuda_worker.seam_crossover(
        left_items,
        right_items,
        seam_seconds=120.0,
        shared_start=90.0,
        shared_end=150.0,
        left_ownership_start=0.0,
        right_ownership_end=240.0,
    )
    args, backend_options, document = completed_two_chunk_raw_fixture(
        chunk_context=30.0,
        left_items=left_items,
        right_items=right_items,
        left_stop=left_stop,
        right_start=right_start,
        seam_record=record,
    )
    return args, backend_options, document, left_items, right_items


def aligned_document_for_two_chunk_fixture(
    raw_document: dict[str, object],
    *,
    left_items: list[dict[str, object]],
    right_items: list[dict[str, object]],
    raw_output_path: Path,
) -> dict[str, object]:
    raw_segments = raw_document["segments"]
    if not isinstance(raw_segments, list):
        raise AssertionError("fixture raw segments must be a list")
    item_sets = (left_items, right_items)
    chunks: list[dict[str, object]] = []
    for raw_chunk, items in zip(raw_segments, item_sets, strict=True):
        if not isinstance(raw_chunk, dict):
            raise AssertionError("fixture raw chunk must be an object")
        owned_start = int(raw_chunk["owned_item_start"])
        owned_stop = int(raw_chunk["owned_item_stop"])
        owned_alignment = copy.deepcopy(items[owned_start:owned_stop])
        chunks.append(
            {
                "decode_start": raw_chunk["decode_start"],
                "decode_end": raw_chunk["decode_end"],
                "decoded_text": raw_chunk["decoded_text"],
                "owned_item_start": owned_start,
                "owned_item_stop": owned_stop,
                "text": "".join(
                    str(item["text"]) for item in owned_alignment
                ),
                "alignment": owned_alignment,
            }
        )
    raw_options = raw_document["options"]
    if not isinstance(raw_options, dict):
        raise AssertionError("fixture raw options must be an object")
    return {
        "options": {
            "final_outro_exemption_seconds": raw_options[
                "final_outro_exemption_seconds"
            ]
        },
        "source": {
            "raw_asr_path": cuda_worker.repository_path(raw_output_path),
        },
        "chunks": chunks,
    }


class ArgumentAndResultValidationTests(unittest.TestCase):
    def test_cli_defaults_to_bfloat16_batch_one_configuration(self) -> None:
        argv = [
            "transcribe_qwen3_asr_cuda.py",
            "--input",
            "source.m4a",
            "--output",
            "raw.json",
            "--aligned-output",
            "aligned.json",
        ]
        with patch.object(cuda_worker.sys, "argv", argv):
            args = cuda_worker.parse_args()

        self.assertEqual(args.dtype, "bfloat16")
        self.assertEqual(args.chunk_duration, 120.0)
        self.assertEqual(args.chunk_context, 5.0)
        self.assertEqual(args.final_outro_exemption_seconds, 0.0)
        self.assertEqual(cuda_worker.MAX_INFERENCE_BATCH_SIZE, 1)

    def test_chunks_audio_with_bounded_context_and_gapless_ownership(self) -> None:
        self.assertEqual(
            list(
                cuda_worker.audio_chunk_ranges(
                    250.0,
                    chunk_duration=120.0,
                    chunk_context=5.0,
                )
            ),
            [
                cuda_worker.AudioChunkWindow(0.0, 120.0, 0.0, 125.0),
                cuda_worker.AudioChunkWindow(120.0, 185.0, 115.0, 190.0),
                cuda_worker.AudioChunkWindow(185.0, 250.0, 180.0, 250.0),
            ],
        )

    def test_rebalances_a_short_final_remainder_across_the_last_two_chunks(self) -> None:
        windows = list(
            cuda_worker.audio_chunk_ranges(
                2171.5,
                chunk_duration=120.0,
                chunk_context=5.0,
            )
        )

        self.assertEqual(len(windows), 19)
        self.assertEqual(
            windows[-2:],
            [
                cuda_worker.AudioChunkWindow(2040.0, 2105.75, 2035.0, 2110.75),
                cuda_worker.AudioChunkWindow(2105.75, 2171.5, 2100.75, 2171.5),
            ],
        )
        self.assertTrue(
            all(
                window.ownership_end - window.ownership_start <= 120.0
                and window.decode_end - window.decode_start <= 130.0
                for window in windows
            )
        )

    def test_allows_sample_rounding_at_the_final_decode_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            backend_options = cuda_worker.raw_backend_options(args)
            document = {
                "audio": {
                    "sample_rate_hz": cuda_worker.SAMPLE_RATE,
                    "duration_seconds": 2.001,
                },
                "options": {
                    "temperature": args.temperature,
                    "max_tokens_per_chunk": args.max_tokens,
                    "chunk_duration_seconds": args.chunk_duration,
                    "chunk_context_seconds": args.chunk_context,
                    "boundary_reconciliation": (
                        cuda_worker.BOUNDARY_RECONCILIATION_METHOD
                    ),
                    "alignment_coverage_guard": cuda_worker.ALIGNMENT_COVERAGE_GUARD,
                    "aligned_gap_guard": cuda_worker.ALIGNED_GAP_GUARD,
                    **backend_options,
                },
                "boundary_reconciliation": {
                    "method": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
                    "status": "pending",
                    "chunk_context_seconds": args.chunk_context,
                    "seams": [],
                },
                "text": "Test.",
                "segments": [
                    {
                        "id": 0,
                        "start": 0.0,
                        "end": 2.001,
                        "decode_start": 0.0,
                        "decode_end": 2.0,
                        "decoded_text": "Test.",
                        "text": "Test.",
                    }
                ],
            }

            cuda_worker.validate_cuda_raw_integrity(
                document,
                args=args,
                backend_options=backend_options,
            )

    def test_allows_bounded_container_shortfall_only_at_final_decode_end(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            backend_options = cuda_worker.raw_backend_options(args)
            duration_seconds = 3598.1
            windows = list(
                cuda_worker.audio_chunk_ranges(
                    duration_seconds,
                    chunk_duration=args.chunk_duration,
                    chunk_context=args.chunk_context,
                )
            )
            segments = [
                {
                    "id": index,
                    "start": cuda_worker.rounded_seconds(window.ownership_start),
                    "end": cuda_worker.rounded_seconds(window.ownership_end),
                    "decode_start": cuda_worker.rounded_seconds(window.decode_start),
                    "decode_end": cuda_worker.rounded_seconds(window.decode_end),
                    "decoded_text": "Test.",
                    "text": "Test.",
                }
                for index, window in enumerate(windows)
            ]
            # Real #20 shape: ffprobe reports 3598.100s, while the final
            # 16 kHz decode contains samples only through 3598.002s.
            segments[-1]["decode_end"] = 3598.002
            document = {
                "audio": {
                    "sample_rate_hz": cuda_worker.SAMPLE_RATE,
                    "duration_seconds": duration_seconds,
                },
                "options": {
                    "temperature": args.temperature,
                    "max_tokens_per_chunk": args.max_tokens,
                    "chunk_duration_seconds": args.chunk_duration,
                    "chunk_context_seconds": args.chunk_context,
                    "boundary_reconciliation": (
                        cuda_worker.BOUNDARY_RECONCILIATION_METHOD
                    ),
                    "alignment_coverage_guard": cuda_worker.ALIGNMENT_COVERAGE_GUARD,
                    "aligned_gap_guard": cuda_worker.ALIGNED_GAP_GUARD,
                    **backend_options,
                },
                "boundary_reconciliation": {
                    "method": cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
                    "status": "pending",
                    "chunk_context_seconds": args.chunk_context,
                    "seams": [],
                },
                "text": cuda_worker.join_transcript_chunks(
                    [segment["text"] for segment in segments],
                    language=args.language,
                ),
                "segments": segments,
            }

            cuda_worker.validate_cuda_raw_integrity(
                document,
                args=args,
                backend_options=backend_options,
            )

            internal_shortfall = copy.deepcopy(document)
            internal_shortfall["segments"][0]["decode_end"] = 124.989
            with self.assertRaisesRegex(ValueError, "invalid ownership"):
                cuda_worker.validate_cuda_raw_integrity(
                    internal_shortfall,
                    args=args,
                    backend_options=backend_options,
                )

            excessive_final_shortfall = copy.deepcopy(document)
            excessive_final_shortfall["segments"][-1]["decode_end"] = 3597.974
            with self.assertRaisesRegex(ValueError, "invalid ownership"):
                cuda_worker.validate_cuda_raw_integrity(
                    excessive_final_shortfall,
                    args=args,
                    backend_options=backend_options,
                )

    def test_reconciles_an_exact_time_constrained_boundary_once(self) -> None:
        left = [
            {"text": "它", "start": 119.5, "end": 119.8},
            {"text": "离", "start": 119.8, "end": 120.1},
            {"text": "呃", "start": 120.6, "end": 120.9},
            {"text": "上", "start": 120.9, "end": 121.1},
        ]
        right = [
            {"text": "它", "start": 119.45, "end": 119.75},
            {"text": "离", "start": 119.78, "end": 120.12},
            {"text": "呃", "start": 120.65, "end": 120.85},
            {"text": "上", "start": 120.92, "end": 121.08},
        ]

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(left_stop, 2)
        self.assertEqual(right_start, 2)
        self.assertEqual(
            "".join(item["text"] for item in left[:left_stop])
            + "".join(item["text"] for item in right[right_start:]),
            "它离呃上",
        )
        self.assertEqual(record["strategy"], "exact-time-anchor")

    def test_rejects_same_text_outside_the_time_gate(self) -> None:
        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                [{"text": "甲", "start": 119.0, "end": 121.0}],
                [{"text": "甲", "start": 125.0, "end": 127.0}],
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=130.0,
            )

    def test_does_not_choose_an_isolated_filler_over_a_reliable_match_run(self) -> None:
        left = [
            {"text": "甲", "start": 117.1, "end": 117.3},
            {"text": "乙", "start": 117.3, "end": 117.5},
            {"text": "丙", "start": 117.5, "end": 117.7},
            {"text": "嗯", "start": 119.8, "end": 120.0},
        ]
        right = [
            {"text": "甲", "start": 117.15, "end": 117.35},
            {"text": "乙", "start": 117.35, "end": 117.55},
            {"text": "丙", "start": 117.55, "end": 117.75},
            {"text": "啊", "start": 119.5, "end": 119.7},
            {"text": "嗯", "start": 119.85, "end": 120.05},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(record["anchor_text"], "丙")
        self.assertEqual(record["anchor_run_characters"], 3)

    def test_ignores_repeated_phrase_candidates_outside_the_seam_search_window(
        self,
    ) -> None:
        left = [
            {"text": "a", "start": 115.0, "end": 115.1},
            {"text": "b", "start": 115.1, "end": 115.2},
            {"text": "c", "start": 115.2, "end": 115.3},
            {"text": "x", "start": 119.6, "end": 119.7},
            {"text": "y", "start": 119.9, "end": 120.0},
            {"text": "z", "start": 120.2, "end": 120.3},
        ]
        right = [
            {"text": "a", "start": 114.95, "end": 115.05},
            {"text": "b", "start": 115.05, "end": 115.15},
            {"text": "c", "start": 115.15, "end": 115.25},
            {"text": "a", "start": 115.35, "end": 115.45},
            {"text": "b", "start": 115.45, "end": 115.55},
            {"text": "c", "start": 115.55, "end": 115.65},
            {"text": "x", "start": 119.65, "end": 119.75},
            {"text": "y", "start": 119.95, "end": 120.05},
            {"text": "z", "start": 120.25, "end": 120.35},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=114.0,
            shared_end=126.0,
        )

        self.assertEqual(record["strategy"], "exact-time-anchor")
        self.assertEqual(record["anchor_run_characters"], 3)
        self.assertIn(record["anchor_text"], {"x", "y", "z"})

    def test_repairs_the_observed_right_extra_repeated_token_indel_bubble(
        self,
    ) -> None:
        left_core, right_core = observed_right_extra_indel_items()
        left = [
            {"text": "左", "start": 1229.0, "end": 1229.01}
            for _ in range(394)
        ] + left_core
        right = [
            {"text": "右", "start": 1229.0, "end": 1229.01}
            for _ in range(144)
        ] + right_core

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=1260.0,
            shared_start=1230.0,
            shared_end=1290.0,
        )

        self.assertEqual((left_stop, right_start), (397, 147))
        self.assertEqual(
            "".join(str(item["text"]) for item in left[394:left_stop])
            + "".join(str(item["text"]) for item in right[right_start:159]),
            "虽然我我我这几天一直在遇到很多",
        )
        self.assertEqual(record["strategy"], "exact-time-anchor")
        self.assertEqual(
            record["ambiguity_resolution"],
            cuda_worker.REPEATED_TOKEN_INDEL_AMBIGUITY_RESOLUTION,
        )
        repair = record["match_run_repair"]
        self.assertEqual(
            repair["method"],
            cuda_worker.REPEATED_TOKEN_INDEL_AMBIGUITY_RESOLUTION,
        )
        self.assertEqual(repair["indel_side"], "right")
        self.assertEqual(repair["repeated_text"], "我")
        self.assertEqual(repair["diagonal_offsets"], [-250, -249])
        self.assertEqual(repair["discarded_candidate_pair_count"], 2)
        self.assertEqual(
            repair["earlier_run"],
            {
                "left": [394, 397],
                "right": [144, 147],
                "characters": 4,
                "max_pair_delta_seconds": 0.04,
            },
        )
        self.assertEqual(repair["later_run_before"]["left"], [396, 407])
        self.assertEqual(repair["later_run_before"]["right"], [147, 158])
        self.assertEqual(
            repair["alternative_delta_margin_seconds"],
            {"minimum": 0.16, "mean": 0.32, "maximum": 0.48},
        )
        self.assertEqual(
            repair["resulting_cut"],
            {"left_stop": left_stop, "right_start": right_start},
        )
        self.assertTrue(repair["ownership_cut_consistent"])

    def test_repeated_token_indel_repair_rejects_every_narrow_gate_violation(
        self,
    ) -> None:
        cases: list[
            tuple[
                str,
                list[dict[str, object]],
                list[dict[str, object]],
                list[tuple[list[tuple[int, int]], int, float]],
            ]
        ] = []

        low_margin_left, low_margin_right = observed_right_extra_indel_items()
        low_margin_left[2] = {
            **low_margin_left[2],
            "start": 1259.98,
            "end": 1260.02,
        }
        cases.append(
            (
                "mean timing margin below 250 ms",
                low_margin_left,
                low_margin_right,
                observed_right_extra_indel_runs(
                    low_margin_left,
                    low_margin_right,
                ),
            )
        )

        nonidentical_left, nonidentical_right = observed_right_extra_indel_items()
        nonidentical_right[4] = {**nonidentical_right[4], "text": "你"}
        cases.append(
            (
                "bubble tokens are not identical",
                nonidentical_left,
                nonidentical_right,
                observed_right_extra_indel_runs(
                    nonidentical_left,
                    nonidentical_right,
                ),
            )
        )

        offset_left, offset_right = observed_right_extra_indel_items()
        offset_right.append(
            {"text": "尾", "start": 1263.0, "end": 1263.04}
        )
        offset_later_run = [(2 + index, 4 + index) for index in range(12)]
        cases.append(
            (
                "diagonal offset differs by two",
                offset_left,
                offset_right,
                observed_right_extra_indel_runs(
                    offset_left,
                    offset_right,
                    later_run=offset_later_run,
                ),
            )
        )

        long_trim_left, long_trim_right = observed_right_extra_indel_items()
        long_trim_earlier_run = [(index, index) for index in range(5)]
        cases.append(
            (
                "repair would trim three pairs",
                long_trim_left,
                long_trim_right,
                observed_right_extra_indel_runs(
                    long_trim_left,
                    long_trim_right,
                    earlier_run=long_trim_earlier_run,
                ),
            )
        )

        crossing_left, crossing_right = observed_right_extra_indel_items()
        crossing_runs = observed_right_extra_indel_runs(
            crossing_left,
            crossing_right,
        )
        crossing_run = [(4 + index, 4 + index) for index in range(3)]
        crossing_runs.append(
            (
                crossing_run,
                cuda_worker._match_run_characters(
                    crossing_run,
                    list(enumerate(crossing_left)),
                ),
                cuda_worker._match_run_max_pair_delta(
                    crossing_run,
                    list(enumerate(crossing_left)),
                    list(enumerate(crossing_right)),
                ),
            )
        )
        cases.append(
            (
                "another candidate still crosses after repair",
                crossing_left,
                crossing_right,
                crossing_runs,
            )
        )

        for label, left, right, runs in cases:
            with self.subTest(label=label):
                self.assertIsNone(
                    cuda_worker._repair_right_extra_repeated_token_indel_bubble(
                        runs,
                        list(enumerate(left)),
                        list(enumerate(right)),
                    )
                )

    def test_repairs_observed_zero_duration_right_indel_weak_bridge(
        self,
    ) -> None:
        left, right = observed_zero_duration_right_indel_bridge_items()

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=480.0,
            shared_start=475.0,
            shared_end=485.0,
        )

        self.assertEqual((left_stop, right_start), (338, 32))
        self.assertEqual(
            "".join(str(item["text"]) for item in left[319:left_stop])
            + "".join(str(item["text"]) for item in right[right_start:48]),
            "因为刚才会长也问了一个问题说他很也说"
            "他很喜欢就是我很好奇啊这个从我认识",
        )
        self.assertEqual(record["anchor_text"], "很")
        self.assertEqual(record["anchor_midpoint_seconds"], 480.04)
        self.assertEqual(record["anchor_run_characters"], 17)
        self.assertEqual(
            record["ambiguity_resolution"],
            cuda_worker.ZERO_DURATION_RIGHT_INDEL_AMBIGUITY_RESOLUTION,
        )
        repair = record["match_run_repair"]
        self.assertEqual(
            set(repair),
            {
                "method",
                "indel_side",
                "candidate_proof",
                "selected_anchor_source",
                "selected_anchor_pair",
                "resulting_cut",
            },
        )
        self.assertEqual(
            repair["resulting_cut"],
            {"left_stop": 338, "right_start": 32},
        )
        proof = repair["candidate_proof"]
        self.assertEqual(proof["window_seconds"], [477.0, 483.0])
        inserted = next(
            item
            for item in proof["right_items"]
            if item["global_index"] == 30
        )
        self.assertEqual(
            inserted,
            {
                "side": "right",
                "global_index": 30,
                "decoded_character_span": [30, 31],
                "cleaned_text": "了",
                "start_seconds": 479.88,
                "end_seconds": 479.88,
            },
        )
        cuda_worker._validate_zero_duration_right_indel_candidate_proof(
            record,
            index=7,
            left_segment={
                "decode_start": 475.0,
                "decode_end": 485.0,
                "decoded_text": "".join(str(item["text"]) for item in left),
            },
            right_segment={
                "decode_start": 475.0,
                "decode_end": 485.0,
                "decoded_text": "".join(str(item["text"]) for item in right),
            },
        )

    def test_zero_duration_right_indel_bridge_rejects_nearby_shapes(
        self,
    ) -> None:
        def reliable_shape(
            left: list[dict[str, object]],
            right: list[dict[str, object]],
        ) -> tuple[
            list[tuple[int, dict[str, object]]],
            list[tuple[int, dict[str, object]]],
            list[tuple[list[tuple[int, int]], int, float]],
        ]:
            left_overlap = [
                (item_index, item)
                for item_index, item in enumerate(left)
                if 477.0
                <= cuda_worker.alignment_item_midpoint(item)
                <= 483.0
            ]
            right_overlap = [
                (item_index, item)
                for item_index, item in enumerate(right)
                if 477.0
                <= cuda_worker.alignment_item_midpoint(item)
                <= 483.0
            ]
            runs = []
            for run in cuda_worker._maximal_exact_match_runs(
                left_overlap,
                right_overlap,
                tolerance_seconds=cuda_worker.SEAM_MATCH_TOLERANCE_SECONDS,
            ):
                characters = cuda_worker._match_run_characters(run, left_overlap)
                if characters < cuda_worker.MIN_SEAM_ANCHOR_RUN_CHARACTERS:
                    continue
                runs.append(
                    (
                        run,
                        characters,
                        cuda_worker._match_run_max_pair_delta(
                            run,
                            left_overlap,
                            right_overlap,
                        ),
                    )
                )
            return left_overlap, right_overlap, runs

        baseline_left, baseline_right = (
            observed_zero_duration_right_indel_bridge_items()
        )
        left_overlap, right_overlap, baseline_runs = reliable_shape(
            baseline_left,
            baseline_right,
        )
        self.assertIsNotNone(
            cuda_worker._repair_zero_duration_right_indel_weak_bridge(
                baseline_runs,
                left_overlap,
                right_overlap,
            )
        )

        nonzero_left = copy.deepcopy(baseline_left)
        nonzero_right = copy.deepcopy(baseline_right)
        nonzero_right[30]["end"] = 479.89
        nonzero_shape = reliable_shape(nonzero_left, nonzero_right)

        detached_left = copy.deepcopy(baseline_left)
        detached_right = copy.deepcopy(baseline_right)
        detached_right[30]["start"] = 479.90
        detached_right[30]["end"] = 479.90
        detached_shape = reliable_shape(detached_left, detached_right)

        low_margin_left = copy.deepcopy(baseline_left)
        low_margin_right = copy.deepcopy(baseline_right)
        for items, item_index in (
            (low_margin_left, 338),
            (low_margin_right, 32),
        ):
            items[item_index] = {
                **items[item_index],
                "start": 479.54,
                "end": 479.58,
            }
        low_margin_shape = reliable_shape(low_margin_left, low_margin_right)

        weak_index = next(
            run_index
            for run_index, (_, characters, _) in enumerate(baseline_runs)
            if characters == 3
        )
        weak_run, _, weak_delta = baseline_runs[weak_index]
        four_character_runs = copy.deepcopy(baseline_runs)
        four_character_runs[weak_index] = (
            [*weak_run, (weak_run[-1][0] + 1, weak_run[-1][1] + 1)],
            4,
            weak_delta,
        )

        uncovered_left_overlap = copy.deepcopy(left_overlap)
        uncovered_start = len(uncovered_left_overlap)
        for offset, (text, midpoint) in enumerate(
            zip("说他很", [480.72, 480.84, 480.96], strict=True)
        ):
            uncovered_left_overlap.append(
                (
                    354 + offset,
                    {
                        "text": text,
                        "start": midpoint - 0.02,
                        "end": midpoint + 0.02,
                    },
                )
            )
        uncovered_runs = copy.deepcopy(baseline_runs)
        uncovered_runs[weak_index] = (
            [
                (uncovered_start + offset, weak_run[offset][1])
                for offset in range(3)
            ],
            3,
            1.92,
        )

        extra_runs = [*copy.deepcopy(baseline_runs), baseline_runs[0]]
        cases = [
            ("nonzero inserted item", *nonzero_shape),
            ("zero-duration item is detached from the junction", *detached_shape),
            ("one weak pair lacks timing advantage", *low_margin_shape),
            (
                "four-character weak run",
                left_overlap,
                right_overlap,
                four_character_runs,
            ),
            (
                "weak left indices are not covered",
                uncovered_left_overlap,
                right_overlap,
                uncovered_runs,
            ),
            ("an extra run remains", left_overlap, right_overlap, extra_runs),
        ]
        for label, selected_left, selected_right, selected_runs in cases:
            with self.subTest(label=label):
                self.assertIsNone(
                    cuda_worker._repair_zero_duration_right_indel_weak_bridge(
                        selected_runs,
                        selected_left,
                        selected_right,
                    )
                )
        with self.assertRaisesRegex(ValueError, "ambiguous exact alignment"):
            cuda_worker.seam_crossover(
                nonzero_left,
                nonzero_right,
                seam_seconds=480.0,
                shared_start=475.0,
                shared_end=485.0,
            )

    def test_repairs_four_observed_single_axis_weak_run_seams(self) -> None:
        expected = {
            "5": ((649, 36), (3, 36), "a927048f1961c77d671e0cb4e5514b6b59547abbf4c8f80e7293702ccd4a0ac4"),
            "12": ((668, 30), (2, 35), "cf3f7f77db47ebcd78b250872df15a7c1bea6ee4c0a92fc3907c50707ee591fa"),
            "13": ((566, 22), (3, 29), "722932efb5b3cb4c615cbd27b7d44e03bd6175e1a14abd6522f9745213b5626b"),
            "14": ((524, 18), (2, 26), "0c545ef850683700add235b36e04fccb368fd943f86da3c78a45f9b908638ca4"),
        }
        for case, (cut, counts, text_sha256) in expected.items():
            with self.subTest(case=case):
                left, right, seam, observed_cut = (
                    observed_single_axis_weak_run_items(case)
                )
                left_stop, right_start, record = cuda_worker.seam_crossover(
                    left,
                    right,
                    seam_seconds=seam,
                    shared_start=seam - 5.0,
                    shared_end=seam + 5.0,
                )
                self.assertEqual(observed_cut, cut)
                self.assertEqual((left_stop, right_start), cut)
                self.assertEqual(
                    record["ambiguity_resolution"],
                    cuda_worker.SINGLE_AXIS_WEAK_RUN_AMBIGUITY_RESOLUTION,
                )
                self.assertEqual(
                    (
                        record["ambiguity_checked_run_count"],
                        record["ambiguity_checked_pair_count"],
                    ),
                    counts,
                )
                repair = record["match_run_repair"]
                self.assertEqual(
                    set(repair),
                    {
                        "method",
                        "candidate_proof",
                        "selected_anchor_source",
                        "selected_anchor_pair",
                        "resulting_cut",
                    },
                )
                self.assertEqual(
                    hashlib.sha256(
                        (
                            "".join(str(item["text"]) for item in left[:left_stop])
                            + "".join(
                                str(item["text"])
                                for item in right[right_start:]
                            )
                        ).encode("utf-8")
                    ).hexdigest(),
                    text_sha256,
                )
                cuda_worker._validate_single_axis_weak_run_candidate_proof(
                    record,
                    index=int(case),
                    left_segment={
                        "decode_start": seam - 5.0,
                        "decode_end": seam + 5.0,
                        "decoded_text": "".join(
                            str(item["text"]) for item in left
                        ),
                    },
                    right_segment={
                        "decode_start": seam - 5.0,
                        "decode_end": seam + 5.0,
                        "decoded_text": "".join(
                            str(item["text"]) for item in right
                        ),
                    },
                )

    def test_single_axis_weak_run_repair_rejects_nearby_shapes(self) -> None:
        left, right, seam, _ = observed_single_axis_weak_run_items("12")
        left_overlap = [
            (item_index, item)
            for item_index, item in enumerate(left)
            if seam - 3.0
            <= cuda_worker.alignment_item_midpoint(item)
            <= seam + 3.0
        ]
        right_overlap = [
            (item_index, item)
            for item_index, item in enumerate(right)
            if seam - 3.0
            <= cuda_worker.alignment_item_midpoint(item)
            <= seam + 3.0
        ]
        _, _, runs = cuda_worker._reliable_match_run_stages(
            left_overlap,
            right_overlap,
            seam_seconds=seam,
        )
        weak_index = next(
            run_index
            for run_index, (_, characters, maximum_delta) in enumerate(runs)
            if characters == 3 and maximum_delta > 0.4
        )
        tight_indices = [
            run_index
            for run_index, (_, _, maximum_delta) in enumerate(runs)
            if maximum_delta <= 0.25
        ]
        self.assertIsNotNone(
            cuda_worker._repair_single_axis_dominated_weak_runs(
                runs,
                left_overlap,
                right_overlap,
                seam_seconds=seam,
            )
        )

        only_one_tight = [runs[weak_index], runs[tight_indices[-1]]]
        short_dominator = copy.deepcopy(runs)
        tight_run, _, tight_delta = short_dominator[tight_indices[-1]]
        short_dominator[tight_indices[-1]] = (tight_run, 5, tight_delta)

        missing_axis_index = copy.deepcopy(runs)
        weak_run, weak_characters, weak_delta = missing_axis_index[weak_index]
        left_local_by_global = {
            global_index: local_index
            for local_index, (global_index, _) in enumerate(left_overlap)
        }
        missing_axis_index[weak_index] = (
            [
                *weak_run[:-1],
                (left_local_by_global[666], weak_run[-1][1]),
            ],
            weak_characters,
            weak_delta,
        )

        union_only = copy.deepcopy(runs)
        union_only[weak_index] = (
            [
                (left_local_by_global[663], weak_run[0][1]),
                *weak_run[1:],
            ],
            weak_characters,
            weak_delta,
        )

        weak_pair_not_loose_left = copy.deepcopy(left_overlap)
        weak_left_local = weak_run[0][0]
        weak_right_item = right_overlap[weak_run[0][1]][1]
        weak_midpoint = cuda_worker.alignment_item_midpoint(weak_right_item) + 0.4
        weak_pair_not_loose_left[weak_left_local] = (
            weak_pair_not_loose_left[weak_left_local][0],
            {
                **weak_pair_not_loose_left[weak_left_local][1],
                "start": weak_midpoint - 0.02,
                "end": weak_midpoint + 0.02,
            },
        )

        insufficient_margin_right = copy.deepcopy(right_overlap)
        right_local_by_global = {
            global_index: local_index
            for local_index, (global_index, _) in enumerate(right_overlap)
        }
        strong_right_local = right_local_by_global[31]
        insufficient_margin_right[strong_right_local] = (
            31,
            {
                **insufficient_margin_right[strong_right_local][1],
                "start": seam - 0.02,
                "end": seam + 0.02,
            },
        )

        uncovered_three = copy.deepcopy(runs)
        first_tight_run, first_tight_characters, first_tight_delta = (
            uncovered_three[tight_indices[0]]
        )
        uncovered_three[tight_indices[0]] = (
            first_tight_run[:-1],
            first_tight_characters - 1,
            first_tight_delta,
        )

        noncontiguous_gap = copy.deepcopy(runs)
        noncontiguous_gap[weak_index] = (
            [
                (weak_run[0][0], right_local_by_global[27]),
                (weak_run[1][0], right_local_by_global[29]),
                (weak_run[2][0], right_local_by_global[48]),
            ],
            weak_characters,
            weak_delta,
        )
        outside_gap = copy.deepcopy(runs)
        outside_gap[weak_index] = (
            [
                (weak_run[offset][0], right_local_by_global[46 + offset])
                for offset in range(3)
            ],
            weak_characters,
            weak_delta,
        )

        crossing_tight = [*copy.deepcopy(runs), copy.deepcopy(runs[tight_indices[0]])]
        retained_conflict = copy.deepcopy(runs)
        retained_conflict.append(
            (
                [runs[tight_indices[-1]][0][0], *weak_run[1:]],
                3,
                0.8,
            )
        )
        cases = [
            ("only one tight run", only_one_tight, left_overlap, right_overlap),
            ("strong run below two-times weak", short_dominator, left_overlap, right_overlap),
            ("dominator axis misses one index", missing_axis_index, left_overlap, right_overlap),
            ("only the tight union covers the axis", union_only, left_overlap, right_overlap),
            ("one weak pair is not loose", runs, weak_pair_not_loose_left, right_overlap),
            ("one pair lacks margin", runs, left_overlap, insufficient_margin_right),
            ("three other-axis indices are uncovered", uncovered_three, left_overlap, right_overlap),
            ("other-axis gap is not contiguous", noncontiguous_gap, left_overlap, right_overlap),
            ("other-axis gap is outside the backbone", outside_gap, left_overlap, right_overlap),
            ("tight backbone crosses", crossing_tight, left_overlap, right_overlap),
            ("atomic drop leaves a conflict", retained_conflict, left_overlap, right_overlap),
        ]
        for label, selected_runs, selected_left, selected_right in cases:
            with self.subTest(label=label):
                self.assertIsNone(
                    cuda_worker._repair_single_axis_dominated_weak_runs(
                        selected_runs,
                        selected_left,
                        selected_right,
                        seam_seconds=seam,
                    )
                )

        original_anchor = cuda_worker._selected_match_run_anchor(
            runs,
            left_overlap,
            right_overlap,
            seam_seconds=seam - 3.0,
        )
        self.assertIsNotNone(original_anchor)
        original_consistent, _, _ = cuda_worker._ownership_cut_consistency(
            runs,
            left_overlap,
            right_overlap,
            left_stop=original_anchor["cut"][0],
            right_start=original_anchor["cut"][1],
        )
        self.assertTrue(original_consistent)
        self.assertIsNone(
            cuda_worker._repair_single_axis_dominated_weak_runs(
                runs,
                left_overlap,
                right_overlap,
                seam_seconds=seam - 3.0,
            )
        )

        tied_left = copy.deepcopy(left_overlap)
        tied_right = copy.deepcopy(right_overlap)
        tied_run = []
        for offset, text in enumerate("XYZ"):
            tied_left.append(
                (
                    687 + offset,
                    {"text": text, "start": seam - 0.02, "end": seam + 0.02},
                )
            )
            tied_right.append(
                (
                    49 + offset,
                    {"text": text, "start": seam - 0.02, "end": seam + 0.02},
                )
            )
            tied_run.append((len(tied_left) - 1, len(tied_right) - 1))
        self.assertIsNone(
            cuda_worker._repair_single_axis_dominated_weak_runs(
                [*runs, (tied_run, 3, 0.0)],
                tied_left,
                tied_right,
                seam_seconds=seam,
            )
        )

    def test_single_axis_weak_run_proof_rejects_tampering(self) -> None:
        left, right, seam, _ = observed_single_axis_weak_run_items("14")
        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=seam,
            shared_start=seam - 5.0,
            shared_end=seam + 5.0,
        )
        segments = (
            {
                "decode_start": seam - 5.0,
                "decode_end": seam + 5.0,
                "decoded_text": "".join(str(item["text"]) for item in left),
            },
            {
                "decode_start": seam - 5.0,
                "decode_end": seam + 5.0,
                "decoded_text": "".join(str(item["text"]) for item in right),
            },
        )
        cuda_worker._validate_single_axis_weak_run_candidate_proof(
            record,
            index=14,
            left_segment=segments[0],
            right_segment=segments[1],
        )

        cases: list[tuple[str, dict[str, object]]] = []
        window = copy.deepcopy(record)
        window["match_run_repair"]["candidate_proof"]["window_seconds"][0] += 0.1
        cases.append(("window", window))

        proof_index = copy.deepcopy(record)
        proof_index["match_run_repair"]["candidate_proof"]["left_items"][4][
            "global_index"
        ] += 1
        cases.append(("item index", proof_index))

        proof_span = copy.deepcopy(record)
        span = proof_span["match_run_repair"]["candidate_proof"]["left_items"][4][
            "decoded_character_span"
        ]
        span[0] += 1
        span[1] += 1
        cases.append(("item span", proof_span))

        proof_text = copy.deepcopy(record)
        proof_text["match_run_repair"]["candidate_proof"]["right_items"][4][
            "cleaned_text"
        ] = "X"
        cases.append(("item text", proof_text))

        proof_time = copy.deepcopy(record)
        proof_time["match_run_repair"]["candidate_proof"]["right_items"][4][
            "start_seconds"
        ] += 0.3
        cases.append(("item time", proof_time))

        sentinel = copy.deepcopy(record)
        sentinel["match_run_repair"]["candidate_proof"]["left_items"].pop(0)
        cases.append(("sentinel", sentinel))

        gap = copy.deepcopy(record)
        gap_item = next(
            item
            for item in gap["match_run_repair"]["candidate_proof"]["right_items"]
            if item["global_index"] == 16
        )
        gap_item["start_seconds"] += 0.5
        gap_item["end_seconds"] += 0.5
        cases.append(("weak gap", gap))

        selected = copy.deepcopy(record)
        selected["match_run_repair"]["selected_anchor_pair"][0] += 1
        cases.append(("selected pair", selected))

        cut = copy.deepcopy(record)
        cut["match_run_repair"]["resulting_cut"]["right_start"] += 1
        cases.append(("cut", cut))

        counts = copy.deepcopy(record)
        counts["ambiguity_checked_pair_count"] += 1
        cases.append(("post counts", counts))

        for label, tampered in cases:
            with self.subTest(label=label), self.assertRaises(ValueError):
                cuda_worker._validate_single_axis_weak_run_candidate_proof(
                    tampered,
                    index=14,
                    left_segment=segments[0],
                    right_segment=segments[1],
                )

    def test_single_axis_proof_binds_raw_cut_and_owned_alignment(self) -> None:
        left, right, seam, _ = observed_single_axis_weak_run_items("14")
        left = shifted_alignment_items(left, 120.0 - seam)
        right = shifted_alignment_items(right, 120.0 - seam)
        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )
        args, backend_options, document = completed_two_chunk_raw_fixture(
            chunk_context=5.0,
            left_items=left,
            right_items=right,
            left_stop=left_stop,
            right_start=right_start,
            seam_record=record,
        )
        cuda_worker.validate_cuda_raw_integrity(
            document,
            args=args,
            backend_options=backend_options,
        )

        cut = copy.deepcopy(document)
        cut["segments"][0]["owned_item_stop"] += 1
        with self.assertRaisesRegex(ValueError, "cut does not match its chunks"):
            cuda_worker.validate_cuda_raw_integrity(
                cut,
                args=args,
                backend_options=backend_options,
            )

        raw_output_path = ROOT / "single-axis-proof-raw.json"
        aligned = aligned_document_for_two_chunk_fixture(
            document,
            left_items=left,
            right_items=right,
            raw_output_path=raw_output_path,
        )
        cuda_worker.validate_cuda_aligned_integrity(
            aligned,
            raw_output_path=raw_output_path,
            raw_document=document,
        )
        tampered = copy.deepcopy(aligned)
        tampered["chunks"][0]["alignment"][513]["end"] += 0.01
        with self.assertRaisesRegex(ValueError, "proof does not match owned items"):
            cuda_worker.validate_cuda_aligned_integrity(
                tampered,
                raw_output_path=raw_output_path,
                raw_document=document,
            )

    def test_uses_a_unique_tight_anchor_at_an_exhausted_left_frontier(
        self,
    ) -> None:
        left, right = left_exhausted_seam_items()

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=90.0,
            shared_end=150.0,
            left_ownership_start=60.0,
            right_ownership_end=180.0,
        )

        self.assertEqual((left_stop, right_start), (len(left), 3))
        self.assertEqual(
            record["strategy"],
            cuda_worker.EXHAUSTED_SIDE_CONTEXT_ANCHOR_STRATEGY,
        )
        self.assertEqual(
            record["fallback_method"],
            cuda_worker.EXHAUSTED_SIDE_CONTEXT_ANCHOR_METHOD,
        )
        self.assertEqual(record["exhausted_side"], "left")
        self.assertEqual(record["anchor_run_text"], "甲乙丙")
        self.assertEqual(record["anchor_run_characters"], 3)
        self.assertLessEqual(
            record["anchor_run_max_pair_delta_seconds"],
            cuda_worker.STRICT_SEAM_ANCHOR_MAX_DELTA_SECONDS,
        )
        self.assertEqual(record["expanded_run_count"], 1)
        self.assertEqual(record["expanded_pair_count"], 3)
        self.assertEqual(
            record["discarded_exhausted_tail"],
            {"items": 0, "characters": 0, "duration_seconds": 0.0, "text": ""},
        )
        self.assertLessEqual(
            record["handoff_gap_seconds"],
            cuda_worker.MAX_EXHAUSTED_HANDOFF_GAP_SECONDS,
        )
        self.assertTrue(record["ownership_cut_consistent"])

    def test_exhausted_left_fallback_rejects_each_missing_proof(self) -> None:
        ambiguous_left, ambiguous_right = left_exhausted_seam_items(
            edge_text="甲乙丙丁甲乙丙"
        )
        ambiguous_edge_start = len(ambiguous_left) - 7
        for items, index in (
            (ambiguous_left, ambiguous_edge_start),
            (ambiguous_right, 0),
        ):
            items[index] = {
                **items[index],
                "start": float(items[index]["start"]) + 0.1,
                "end": float(items[index]["end"]) + 0.1,
            }
        ambiguous_right[3] = {**ambiguous_right[3], "text": "戊"}
        cases = [
            (
                "shortfall below ten seconds",
                left_exhausted_seam_items(terminal_midpoint=110.5),
            ),
            (
                "right candidate does not span the seam",
                left_exhausted_seam_items(right_crosses_seam=False),
            ),
            (
                "edge anchor has only two characters",
                left_exhausted_seam_items(edge_text="甲乙"),
            ),
            (
                "edge anchor is ambiguous",
                (ambiguous_left, ambiguous_right),
            ),
            (
                "edge anchor exceeds the strict timing gate",
                left_exhausted_seam_items(edge_delta=0.251),
            ),
            (
                "more than one exhausted item would be discarded",
                left_exhausted_seam_items(tail_text="丁戊"),
            ),
            (
                "handoff gap exceeds 750 ms",
                left_exhausted_seam_items(handoff_gap=0.751),
            ),
        ]
        for label, (left, right) in cases:
            with self.subTest(label=label), self.assertRaises(ValueError):
                cuda_worker.seam_crossover(
                    left,
                    right,
                    seam_seconds=120.0,
                    shared_start=90.0,
                    shared_end=150.0,
                    left_ownership_start=60.0,
                    right_ownership_end=180.0,
                )

    def test_exhausted_shortfall_is_bounded_from_fifteen_to_twenty_seven_seconds(
        self,
    ) -> None:
        for shortfall, accepted in (
            (14.999, False),
            (15.0, True),
            (27.0, True),
            (27.001, False),
        ):
            left, right = left_exhausted_seam_items(
                terminal_midpoint=120.0 - shortfall - 0.02,
            )
            with self.subTest(shortfall=shortfall):
                if not accepted:
                    with self.assertRaises(ValueError):
                        cuda_worker.seam_crossover(
                            left,
                            right,
                            seam_seconds=120.0,
                            shared_start=90.0,
                            shared_end=150.0,
                            left_ownership_start=60.0,
                            right_ownership_end=180.0,
                        )
                    continue
                _, _, record = cuda_worker.seam_crossover(
                    left,
                    right,
                    seam_seconds=120.0,
                    shared_start=90.0,
                    shared_end=150.0,
                    left_ownership_start=60.0,
                    right_ownership_end=180.0,
                )
                self.assertEqual(
                    record["strategy"],
                    cuda_worker.EXHAUSTED_SIDE_CONTEXT_ANCHOR_STRATEGY,
                )
                self.assertAlmostEqual(
                    record["uncovered_to_seam_seconds"],
                    shortfall,
                    places=3,
                )

    def test_exhausted_shortfall_minimum_scales_with_core_duration(self) -> None:
        def candidate(
            *,
            core_seconds: float,
            shortfall: float,
        ) -> tuple[
            list[dict[str, object]],
            list[dict[str, object]],
            int,
            int,
            dict[str, object],
        ]:
            left, right = left_exhausted_seam_items(
                terminal_midpoint=120.0 - shortfall - 0.02,
            )
            if core_seconds == 120.0:
                left = alignment_items_at_midpoints(
                    "".join(chr(0x5900 + index) for index in range(30)),
                    [0.5 + 2.0 * index for index in range(30)],
                ) + left
            left_stop, right_start, record = cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=90.0,
                shared_end=150.0,
                left_ownership_start=120.0 - core_seconds,
                right_ownership_end=120.0 + core_seconds,
            )
            return left, right, left_stop, right_start, record

        for core_seconds, rejected, accepted in (
            (120.0, 17.999, 18.0),
            (60.0, 14.999, 15.0),
        ):
            with self.subTest(core_seconds=core_seconds, shortfall=rejected):
                with self.assertRaises(ValueError):
                    candidate(
                        core_seconds=core_seconds,
                        shortfall=rejected,
                    )

            left, right, _, _, record = candidate(
                core_seconds=core_seconds,
                shortfall=accepted,
            )
            self.assertAlmostEqual(
                record["uncovered_to_seam_seconds"],
                accepted,
                places=3,
            )
            seam = {
                "left_chunk_id": 0,
                "right_chunk_id": 1,
                **record,
            }
            left_segment = {
                "start": 120.0 - core_seconds,
                "end": 120.0,
                "decode_start": 90.0,
                "decode_end": 150.0,
                "decoded_text": "".join(str(item["text"]) for item in left),
            }
            right_segment = {
                "start": 120.0,
                "end": 120.0 + core_seconds,
                "decode_start": 90.0,
                "decode_end": 150.0,
                "decoded_text": "".join(str(item["text"]) for item in right),
            }
            cuda_worker._validate_exhausted_side_context_anchor(
                seam,
                index=0,
                left_segment=left_segment,
                right_segment=right_segment,
            )

            underflow = copy.deepcopy(seam)
            underflow["terminal_alignment_end_seconds"] = (
                cuda_worker.rounded_seconds(120.0 - rejected)
            )
            underflow["uncovered_to_seam_seconds"] = rejected
            with self.subTest(
                core_seconds=core_seconds,
                validator_shortfall=rejected,
            ), self.assertRaises(ValueError):
                cuda_worker._validate_exhausted_side_context_anchor(
                    underflow,
                    index=0,
                    left_segment=left_segment,
                    right_segment=right_segment,
                )

    def test_exhausted_anchor_pair_accepts_the_strict_delta_boundary(self) -> None:
        for pair_delta in (0.2, 0.25):
            with self.subTest(pair_delta=pair_delta):
                args, backend_options, document, _, _ = (
                    completed_exhausted_fixture(edge_delta=pair_delta)
                )
                seam = document["boundary_reconciliation"]["seams"][0]
                self.assertAlmostEqual(
                    seam["anchor_pair_delta_seconds"],
                    pair_delta,
                    places=3,
                )
                self.assertGreater(
                    seam["anchor_midpoint_seconds"],
                    seam["last_retained_left_end_seconds"],
                )
                self.assertLessEqual(
                    seam["anchor_midpoint_seconds"],
                    seam["last_retained_left_end_seconds"]
                    + seam["anchor_pair_delta_seconds"] / 2.0
                    + 0.001,
                )
                cuda_worker.validate_cuda_raw_integrity(
                    document,
                    args=args,
                    backend_options=backend_options,
                )

        left, right = left_exhausted_seam_items(edge_delta=0.251)
        with self.assertRaises(ValueError):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=90.0,
                shared_end=150.0,
                left_ownership_start=60.0,
                right_ownership_end=180.0,
            )

    def test_exhausted_crossing_item_is_bounded_by_midpoint_not_endpoints(
        self,
    ) -> None:
        args, backend_options, document, _, _ = completed_exhausted_fixture(
            crossing_start=116.9,
            crossing_end=123.1,
        )
        seam = document["boundary_reconciliation"]["seams"][0]
        self.assertEqual(seam["default_window_seconds"], [117.0, 123.0])
        crossing = seam["right_crossing_item"]
        self.assertEqual(crossing["start_seconds"], 116.9)
        self.assertEqual(crossing["end_seconds"], 123.1)
        self.assertEqual(
            (crossing["start_seconds"] + crossing["end_seconds"]) / 2.0,
            120.0,
        )
        cuda_worker.validate_cuda_raw_integrity(
            document,
            args=args,
            backend_options=backend_options,
        )

        left, right = left_exhausted_seam_items(
            crossing_start=119.8,
            crossing_end=126.4,
        )
        with self.assertRaises(ValueError):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=90.0,
                shared_end=150.0,
                left_ownership_start=60.0,
                right_ownership_end=180.0,
            )

    def test_exhausted_bridge_cannot_borrow_a_discarded_crossing_item(self) -> None:
        left, right = left_exhausted_seam_items()
        crossing_index = next(
            index
            for index, item in enumerate(right)
            if float(item["start"]) < 120.0 < float(item["end"])
        )
        discarded_crossing = right.pop(crossing_index)
        right.insert(0, discarded_crossing)
        expected_right_start = 4
        self.assertLess(right.index(discarded_crossing), expected_right_start)
        self.assertFalse(
            any(
                float(item["start"]) < 120.0 < float(item["end"])
                for item in right[expected_right_start:]
            )
        )

        with self.assertRaises(ValueError):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=90.0,
                shared_end=150.0,
                left_ownership_start=60.0,
                right_ownership_end=180.0,
            )

    def test_exhausted_bridge_gap_guard_probes_strictly_over_three_seconds(
        self,
    ) -> None:
        def seam_with_bridge_gap(duration: float) -> dict[str, object]:
            left, right = left_exhausted_seam_items()
            right = [*right[:4], *copy.deepcopy(right[10:])]
            right[4] = {
                **right[4],
                "start": float(right[3]["end"]) + duration,
                "end": float(right[3]["end"]) + duration + 0.04,
            }
            _, _, record = cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=90.0,
                shared_end=150.0,
                left_ownership_start=60.0,
                right_ownership_end=180.0,
            )
            return record

        exactly_three = seam_with_bridge_gap(3.0)
        self.assertEqual(
            exactly_three["bridge_gap_guard"],
            {
                "method": cuda_worker.EXHAUSTED_BRIDGE_GAP_GUARD,
                "status": "verified",
                "maximum_unprobed_gap_seconds": 3.0,
                "maximum_observed_gap_seconds": 3.0,
                "probes": [],
            },
        )

        active = seam_with_bridge_gap(3.001)
        active_guard = active["bridge_gap_guard"]
        self.assertEqual(active_guard["status"], "pending")
        self.assertEqual(
            active_guard["probes"],
            [
                {
                    "start_seconds": 96.34,
                    "end_seconds": 99.341,
                    "duration_seconds": 3.001,
                    "acoustic_status": "pending",
                }
            ],
        )
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.5, 0.5),
            ),
            self.assertRaisesRegex(ValueError, "survivor bridge is not acoustically quiet"),
        ):
            cuda_worker.enforce_exhausted_bridge_gap_silence(
                input_path=Path("source.m4a"),
                seam_records=[active],
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )
        self.assertEqual(active_guard["status"], "pending")

        quiet = seam_with_bridge_gap(3.001)
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.2, 0.2),
            ),
        ):
            cuda_worker.enforce_exhausted_bridge_gap_silence(
                input_path=Path("source.m4a"),
                seam_records=[quiet],
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )
        quiet_guard = quiet["bridge_gap_guard"]
        self.assertEqual(quiet_guard["status"], "verified")
        self.assertEqual(
            quiet_guard["probes"][0],
            {
                "start_seconds": 96.34,
                "end_seconds": 99.341,
                "duration_seconds": 3.001,
                "acoustic_status": "verified-quiet",
                "window_seconds": cuda_worker.GAP_SILENCE_WINDOW_SECONDS,
                "maximum_dbfs": cuda_worker.GAP_SILENCE_DBFS,
                "maximum_active_seconds": cuda_worker.GAP_MAX_ACTIVE_SECONDS,
                "maximum_active_fraction": cuda_worker.GAP_MAX_ACTIVE_FRACTION,
                "active_seconds": 0.2,
                "active_fraction": 0.2,
            },
        )

    def test_indel_validator_rejects_structurally_plausible_tampering(self) -> None:
        left_core, right_core = observed_right_extra_indel_items()
        left = [
            {"text": "左", "start": 1229.0, "end": 1229.01}
            for _ in range(394)
        ] + left_core
        right = [
            {"text": "右", "start": 1229.0, "end": 1229.01}
            for _ in range(144)
        ] + right_core
        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=1260.0,
            shared_start=1230.0,
            shared_end=1290.0,
        )
        cuda_worker._validate_repeated_token_indel_evidence(record, index=0)

        cases: list[tuple[str, dict[str, object]]] = []

        boolean_count = copy.deepcopy(record)
        boolean_count["match_run_repair"]["post_repair_run_count"] = True
        cases.append(("boolean count", boolean_count))

        off_diagonal = copy.deepcopy(record)
        off_diagonal["match_run_repair"]["diagonal_offsets"][1] += 1
        cases.append(("off-diagonal run", off_diagonal))

        shortened_endpoint = copy.deepcopy(record)
        later_after = shortened_endpoint["match_run_repair"]["later_run_after"]
        later_after["left"][1] -= 1
        later_after["right"][1] -= 1
        cases.append(("later-after endpoint", shortened_endpoint))

        top_level_anchor = copy.deepcopy(record)
        top_level_anchor["anchor_run_characters"] += 1
        cases.append(("top-level anchor mismatch", top_level_anchor))

        for label, tampered in cases:
            with self.subTest(label=label), self.assertRaises(ValueError):
                cuda_worker._validate_repeated_token_indel_evidence(
                    tampered,
                    index=0,
                )

    def test_zero_duration_indel_validator_rejects_tampering(self) -> None:
        left, right = observed_zero_duration_right_indel_bridge_items()
        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=480.0,
            shared_start=475.0,
            shared_end=485.0,
        )
        segments = (
            {
                "decode_start": 475.0,
                "decode_end": 485.0,
                "decoded_text": "".join(str(item["text"]) for item in left),
            },
            {
                "decode_start": 475.0,
                "decode_end": 485.0,
                "decoded_text": "".join(str(item["text"]) for item in right),
            },
        )
        cuda_worker._validate_zero_duration_right_indel_candidate_proof(
            record,
            index=7,
            left_segment=segments[0],
            right_segment=segments[1],
        )

        cases: list[tuple[str, dict[str, object]]] = []

        inserted_text = copy.deepcopy(record)
        inserted_proof = inserted_text["match_run_repair"]["candidate_proof"]
        next(
            item
            for item in inserted_proof["right_items"]
            if item["global_index"] == 30
        )["cleaned_text"] = "X"
        cases.append(("coherently forged inserted text", inserted_text))

        shifted_junction = copy.deepcopy(record)
        shifted_proof = shifted_junction["match_run_repair"]["candidate_proof"]
        for side, global_index, field in (
            ("left", 336, "end_seconds"),
            ("left", 337, "start_seconds"),
            ("right", 29, "end_seconds"),
            ("right", 30, "start_seconds"),
            ("right", 30, "end_seconds"),
            ("right", 31, "start_seconds"),
        ):
            item = next(
                item
                for item in shifted_proof[f"{side}_items"]
                if item["global_index"] == global_index
            )
            item[field] += 0.2
        cases.append(("coherently shifted junction axis", shifted_junction))

        forged_deltas = copy.deepcopy(record)
        forged_deltas["anchor_run_max_pair_delta_seconds"] = 0.2
        cases.append(("coherently forged timing deltas", forged_deltas))

        crossing_cut = copy.deepcopy(record)
        crossing_repair = crossing_cut["match_run_repair"]
        crossing_repair["selected_anchor_pair"] = [337, 31]
        crossing_repair["resulting_cut"] = {
            "left_stop": 337,
            "right_start": 31,
        }
        crossing_cut["anchor_text"] = "他"
        crossing_cut["anchor_midpoint_seconds"] = 480.001
        crossing_cut["anchor_run_max_pair_delta_seconds"] = 0.2
        cases.append(("coherently forged anchor and cut", crossing_cut))

        proof_index = copy.deepcopy(record)
        proof_index_items = proof_index["match_run_repair"]["candidate_proof"][
            "right_items"
        ]
        proof_index_items[5]["global_index"] += 1
        cases.append(("proof global index", proof_index))

        proof_time = copy.deepcopy(record)
        proof_time_items = proof_time["match_run_repair"]["candidate_proof"][
            "right_items"
        ]
        next(
            item for item in proof_time_items if item["global_index"] == 30
        )["end_seconds"] = 479.89
        cases.append(("proof inserted duration", proof_time))

        proof_span = copy.deepcopy(record)
        proof_span_items = proof_span["match_run_repair"]["candidate_proof"][
            "right_items"
        ]
        proof_span_items[5]["decoded_character_span"][0] += 1
        proof_span_items[5]["decoded_character_span"][1] += 1
        cases.append(("proof decoded span", proof_span))

        dropped = copy.deepcopy(record)
        dropped["match_run_repair"]["candidate_proof"]["left_items"].pop(4)
        cases.append(("dropped proof item", dropped))

        unknown_field = copy.deepcopy(record)
        unknown_field["match_run_repair"]["unverified"] = True
        cases.append(("unknown evidence field", unknown_field))

        for label, tampered in cases:
            with self.subTest(label=label), self.assertRaises(ValueError):
                cuda_worker._validate_zero_duration_right_indel_candidate_proof(
                    tampered,
                    index=7,
                    left_segment=segments[0],
                    right_segment=segments[1],
                )

    def test_zero_duration_indel_raw_cut_is_bound_to_adjacent_chunks(self) -> None:
        left, right = observed_zero_duration_right_indel_bridge_items()
        left = shifted_alignment_items(left, -360.0)
        right = shifted_alignment_items(right, -360.0)
        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )
        args, backend_options, document = completed_two_chunk_raw_fixture(
            chunk_context=5.0,
            left_items=left,
            right_items=right,
            left_stop=left_stop,
            right_start=right_start,
            seam_record=record,
        )
        cuda_worker.validate_cuda_raw_integrity(
            document,
            args=args,
            backend_options=backend_options,
        )

        for chunk_index, field in (
            (0, "owned_item_stop"),
            (1, "owned_item_start"),
        ):
            tampered = copy.deepcopy(document)
            tampered["segments"][chunk_index][field] += 1
            with self.subTest(field=field), self.assertRaisesRegex(
                ValueError,
                "cut does not match its chunks",
            ):
                cuda_worker.validate_cuda_raw_integrity(
                    tampered,
                    args=args,
                    backend_options=backend_options,
                )

        forged_cut = copy.deepcopy(document)
        forged_seam = forged_cut["boundary_reconciliation"]["seams"][0]
        forged_repair = forged_seam["match_run_repair"]
        forged_repair["selected_anchor_pair"] = [337, 31]
        forged_repair["resulting_cut"] = {
            "left_stop": 337,
            "right_start": 31,
        }
        forged_seam["anchor_text"] = "他"
        forged_seam["anchor_owner"] = "right"
        forged_seam["anchor_midpoint_seconds"] = 120.001
        forged_seam["anchor_run_max_pair_delta_seconds"] = 0.2
        forged_cut["segments"][0]["owned_item_stop"] = 337
        forged_cut["segments"][1]["owned_item_start"] = 31
        forged_cut["segments"][0]["text"] = "".join(
            str(item["text"]) for item in left[:337]
        )
        forged_cut["segments"][1]["text"] = "".join(
            str(item["text"]) for item in right[31:]
        )
        forged_cut["text"] = cuda_worker.join_transcript_chunks(
            [
                forged_cut["segments"][0]["text"],
                forged_cut["segments"][1]["text"],
            ],
            language=args.language,
        )
        with self.assertRaisesRegex(ValueError, "anchor.*not proof-derived"):
            cuda_worker.validate_cuda_raw_integrity(
                forged_cut,
                args=args,
                backend_options=backend_options,
            )

        raw_output_path = ROOT / "zero-duration-proof-raw.json"
        aligned = aligned_document_for_two_chunk_fixture(
            document,
            left_items=left,
            right_items=right,
            raw_output_path=raw_output_path,
        )
        cuda_worker.validate_cuda_aligned_integrity(
            aligned,
            raw_output_path=raw_output_path,
            raw_document=document,
        )

        aligned_text = copy.deepcopy(aligned)
        aligned_text["chunks"][0]["alignment"][319]["text"] = "X"
        aligned_text["chunks"][0]["text"] = "".join(
            str(item["text"])
            for item in aligned_text["chunks"][0]["alignment"]
        )
        aligned_time = copy.deepcopy(aligned)
        aligned_time["chunks"][1]["alignment"][0]["end"] += 0.01
        for label, tampered_aligned in (
            ("owned proof text", aligned_text),
            ("owned proof time", aligned_time),
        ):
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError,
                "proof does not match owned items",
            ):
                cuda_worker.validate_cuda_aligned_integrity(
                    tampered_aligned,
                    raw_output_path=raw_output_path,
                    raw_document=document,
                )

    def test_specialized_raw_cuts_are_bound_to_their_adjacent_chunks(self) -> None:
        left_core, right_core = observed_right_extra_indel_items()
        left = shifted_alignment_items(
            [
                {"text": "左", "start": 1229.0, "end": 1229.01}
                for _ in range(394)
            ]
            + left_core,
            -1140.0,
        )
        right = shifted_alignment_items(
            [
                {"text": "右", "start": 1229.0, "end": 1229.01}
                for _ in range(144)
            ]
            + right_core,
            -1140.0,
        )
        left_stop, right_start, indel_record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )
        args, backend_options, indel_raw = completed_two_chunk_raw_fixture(
            chunk_context=5.0,
            left_items=left,
            right_items=right,
            left_stop=left_stop,
            right_start=right_start,
            seam_record=indel_record,
        )
        cuda_worker.validate_cuda_raw_integrity(
            indel_raw,
            args=args,
            backend_options=backend_options,
        )

        exhausted_args, exhausted_backend, exhausted_raw, _, _ = (
            completed_exhausted_fixture()
        )
        cuda_worker.validate_cuda_raw_integrity(
            exhausted_raw,
            args=exhausted_args,
            backend_options=exhausted_backend,
        )

        for label, baseline, cut_field in (
            ("indel left", indel_raw, (0, "owned_item_stop")),
            ("indel right", indel_raw, (1, "owned_item_start")),
            ("exhausted left", exhausted_raw, (0, "owned_item_stop")),
            ("exhausted right", exhausted_raw, (1, "owned_item_start")),
        ):
            tampered = copy.deepcopy(baseline)
            chunk_index, field = cut_field
            tampered["segments"][chunk_index][field] += 1
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError,
                "cut does not match its chunks",
            ):
                selected_args = args if baseline is indel_raw else exhausted_args
                selected_backend = (
                    backend_options
                    if baseline is indel_raw
                    else exhausted_backend
                )
                cuda_worker.validate_cuda_raw_integrity(
                    tampered,
                    args=selected_args,
                    backend_options=selected_backend,
                )

    def test_exhausted_raw_validator_rejects_forged_bounds_and_bridge_evidence(
        self,
    ) -> None:
        args, backend_options, document, _, _ = completed_exhausted_fixture()
        cuda_worker.validate_cuda_raw_integrity(
            document,
            args=args,
            backend_options=backend_options,
        )

        cases: list[tuple[str, dict[str, object]]] = []

        shared_window = copy.deepcopy(document)
        shared_seam = shared_window["boundary_reconciliation"]["seams"][0]
        shared_seam["shared_window_seconds"] = [89.0, 150.0]
        shared_seam["expanded_window_seconds"] = [89.0, 150.0]
        cases.append(("shared window", shared_window))

        crossing_time = copy.deepcopy(document)
        crossing_time["boundary_reconciliation"]["seams"][0][
            "right_crossing_item"
        ]["start_seconds"] = 120.0
        cases.append(("crossing time", crossing_time))

        crossing_index = copy.deepcopy(document)
        crossing_seam = crossing_index["boundary_reconciliation"]["seams"][0]
        crossing_seam["right_crossing_item"]["index"] = (
            crossing_seam["right_start"] - 1
        )
        cases.append(("crossing index", crossing_index))

        bridge = copy.deepcopy(document)
        bridge_guard = bridge["boundary_reconciliation"]["seams"][0][
            "bridge_gap_guard"
        ]
        bridge_guard["maximum_observed_gap_seconds"] = 25.0
        cases.append(("bridge maximum", bridge))

        for label, tampered in cases:
            with self.subTest(label=label), self.assertRaises(ValueError):
                cuda_worker.validate_cuda_raw_integrity(
                    tampered,
                    args=args,
                    backend_options=backend_options,
                )

    def test_normal_exact_anchor_must_stay_near_seam_and_own_its_side(self) -> None:
        left = [
            {"text": "甲", "start": 119.5, "end": 119.8},
            {"text": "乙", "start": 119.8, "end": 120.1},
            {"text": "丙", "start": 120.6, "end": 120.9},
            {"text": "丁", "start": 120.9, "end": 121.1},
        ]
        right = [
            {"text": "甲", "start": 119.45, "end": 119.75},
            {"text": "乙", "start": 119.78, "end": 120.12},
            {"text": "丙", "start": 120.65, "end": 120.85},
            {"text": "丁", "start": 120.92, "end": 121.08},
        ]
        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )
        args, backend_options, document = completed_two_chunk_raw_fixture(
            chunk_context=5.0,
            left_items=left,
            right_items=right,
            left_stop=left_stop,
            right_start=right_start,
            seam_record=record,
        )
        cuda_worker.validate_cuda_raw_integrity(
            document,
            args=args,
            backend_options=backend_options,
        )

        far_midpoint = copy.deepcopy(document)
        far_midpoint["boundary_reconciliation"]["seams"][0][
            "anchor_midpoint_seconds"
        ] = 124.0
        reversed_owner = copy.deepcopy(document)
        owner_seam = reversed_owner["boundary_reconciliation"]["seams"][0]
        owner_seam["anchor_owner"] = (
            "right" if owner_seam["anchor_owner"] == "left" else "left"
        )

        for label, tampered in (
            ("far midpoint", far_midpoint),
            ("reversed owner", reversed_owner),
        ):
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError,
                "outside its search window",
            ):
                cuda_worker.validate_cuda_raw_integrity(
                    tampered,
                    args=args,
                    backend_options=backend_options,
                )

    def test_aligned_exhausted_evidence_is_recomputed_from_owned_items(self) -> None:
        args, backend_options, raw, left_items, right_items = (
            completed_exhausted_fixture()
        )
        cuda_worker.validate_cuda_raw_integrity(
            raw,
            args=args,
            backend_options=backend_options,
        )
        raw_output_path = ROOT / "fixture-raw.json"
        aligned = aligned_document_for_two_chunk_fixture(
            raw,
            left_items=left_items,
            right_items=right_items,
            raw_output_path=raw_output_path,
        )
        cuda_worker.validate_cuda_aligned_integrity(
            aligned,
            raw_output_path=raw_output_path,
            raw_document=raw,
        )

        cases: list[tuple[str, dict[str, object]]] = []
        before_count = copy.deepcopy(raw)
        before_count["boundary_reconciliation"]["seams"][0][
            "right_default_before_characters"
        ] += 1
        cases.append(("right before characters", before_count))

        after_count = copy.deepcopy(raw)
        after_count["boundary_reconciliation"]["seams"][0][
            "right_default_after_characters"
        ] += 1
        cases.append(("right after characters", after_count))

        crossing = copy.deepcopy(raw)
        crossing["boundary_reconciliation"]["seams"][0][
            "right_crossing_item"
        ]["index"] += 1
        cases.append(("crossing index", crossing))

        bridge = copy.deepcopy(raw)
        bridge["boundary_reconciliation"]["seams"][0]["bridge_gap_guard"][
            "maximum_observed_gap_seconds"
        ] += 0.1
        cases.append(("bridge gaps", bridge))

        for label, tampered_raw in cases:
            with self.subTest(label=label), self.assertRaisesRegex(
                ValueError,
                "evidence does not match owned items|bridge gaps do not match owned items",
            ):
                cuda_worker.validate_cuda_aligned_integrity(
                    aligned,
                    raw_output_path=raw_output_path,
                    raw_document=tampered_raw,
                )

    def test_rejects_ambiguous_three_character_exact_match_runs(self) -> None:
        left = [
            {"text": "a", "start": 119.10, "end": 119.15},
            {"text": "b", "start": 119.20, "end": 119.25},
            {"text": "c", "start": 119.30, "end": 119.35},
            {"text": "X", "start": 120.30, "end": 120.35},
        ]
        right = [
            {"text": "a", "start": 118.95, "end": 119.00},
            {"text": "b", "start": 119.05, "end": 119.10},
            {"text": "c", "start": 119.15, "end": 119.20},
            {"text": "a", "start": 119.35, "end": 119.40},
            {"text": "b", "start": 119.45, "end": 119.50},
            {"text": "c", "start": 119.55, "end": 119.60},
            {"text": "Y", "start": 120.35, "end": 120.40},
        ]

        with self.assertRaisesRegex(ValueError, "ambiguous exact alignment"):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=119.4,
                shared_start=118.5,
                shared_end=120.8,
            )

    def test_accepts_ambiguous_matches_wholly_on_one_ownership_side(self) -> None:
        texts = list("abcabcxyz")
        left = [
            {
                "text": text,
                "start": 119.1 + index * 0.1,
                "end": 119.15 + index * 0.1,
            }
            for index, text in enumerate(texts)
        ]
        right = [
            {
                "text": text,
                "start": 119.11 + index * 0.1,
                "end": 119.16 + index * 0.1,
            }
            for index, text in enumerate(texts)
        ]

        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=118.5,
            shared_end=120.8,
        )

        self.assertEqual((left_stop, right_start), (9, 9))
        self.assertEqual(
            record["ambiguity_resolution"],
            cuda_worker.OWNERSHIP_CUT_AMBIGUITY_RESOLUTION,
        )
        self.assertEqual(record["ambiguity_checked_run_count"], 3)
        self.assertEqual(record["ambiguity_checked_pair_count"], 15)

    def test_ownership_cut_guard_covers_observed_shapes_and_crossings(self) -> None:
        left_overlap = [(index, {}) for index in range(520)]
        right_overlap = [(index, {}) for index in range(190)]

        def diagonal(
            left_start: int,
            left_end: int,
            right_start: int,
            right_end: int,
        ) -> list[tuple[int, int]]:
            self.assertEqual(left_end - left_start, right_end - right_start)
            return list(
                zip(
                    range(left_start, left_end + 1),
                    range(right_start, right_end + 1),
                )
            )

        observed = [
            (
                478,
                174,
                [
                    diagonal(457, 466, 154, 163),
                    diagonal(463, 465, 167, 169),
                    diagonal(469, 492, 165, 188),
                    diagonal(471, 473, 160, 162),
                ],
            ),
            (
                493,
                149,
                [
                    diagonal(474, 492, 130, 148),
                    diagonal(495, 505, 152, 162),
                    diagonal(505, 507, 163, 165),
                ],
            ),
            (
                472,
                166,
                [
                    diagonal(456, 468, 151, 163),
                    diagonal(470, 475, 164, 169),
                    diagonal(475, 477, 170, 172),
                    diagonal(481, 487, 175, 181),
                    diagonal(488, 490, 183, 185),
                ],
            ),
            (
                495,
                164,
                [
                    diagonal(478, 484, 148, 154),
                    diagonal(485, 506, 154, 175),
                ],
            ),
            (
                387,
                128,
                [
                    diagonal(380, 384, 122, 126),
                    diagonal(381, 384, 124, 127),
                    diagonal(381, 383, 125, 127),
                    diagonal(382, 384, 123, 125),
                    diagonal(387, 390, 128, 131),
                    diagonal(394, 396, 135, 137),
                ],
            ),
        ]
        for left_stop, right_start, runs in observed:
            with self.subTest(left_stop=left_stop, right_start=right_start):
                candidates = [(run, len(run), 0.0) for run in runs]
                consistent, checked_runs, checked_pairs = (
                    cuda_worker._ownership_cut_consistency(
                        candidates,
                        left_overlap,
                        right_overlap,
                        left_stop=left_stop,
                        right_start=right_start,
                    )
                )
                self.assertTrue(consistent)
                self.assertEqual(checked_runs, len(runs))
                self.assertEqual(checked_pairs, sum(map(len, runs)))

        crossing_cases = [
            ([(4, 5)], 5, 5),
            ([(5, 4)], 5, 5),
            ([(5, 3)], 5, 4),
            ([(3, 4)], 4, 4),
        ]
        for run, left_stop, right_start in crossing_cases:
            with self.subTest(
                run=run,
                left_stop=left_stop,
                right_start=right_start,
            ):
                consistent, _, _ = cuda_worker._ownership_cut_consistency(
                    [(run, len(run), 0.0)],
                    left_overlap,
                    right_overlap,
                    left_stop=left_stop,
                    right_start=right_start,
                )
                self.assertFalse(consistent)

    def test_accepts_disjoint_ordered_three_character_match_runs(self) -> None:
        left = [
            {"text": "a", "start": 118.9, "end": 118.95},
            {"text": "b", "start": 119.0, "end": 119.05},
            {"text": "c", "start": 119.1, "end": 119.15},
            {"text": "X", "start": 119.8, "end": 119.85},
            {"text": "d", "start": 120.2, "end": 120.25},
            {"text": "e", "start": 120.3, "end": 120.35},
            {"text": "f", "start": 120.4, "end": 120.45},
        ]
        right = [
            {"text": "a", "start": 118.95, "end": 119.0},
            {"text": "b", "start": 119.05, "end": 119.1},
            {"text": "c", "start": 119.15, "end": 119.2},
            {"text": "Y", "start": 119.85, "end": 119.9},
            {"text": "d", "start": 120.25, "end": 120.3},
            {"text": "e", "start": 120.35, "end": 120.4},
            {"text": "f", "start": 120.45, "end": 120.5},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=118.5,
            shared_end=120.8,
        )

        self.assertEqual(record["strategy"], "exact-time-anchor")
        self.assertEqual(record["anchor_run_characters"], 3)

    def test_discards_a_shorter_looser_conflict_inside_one_long_match(self) -> None:
        texts = list("abcdbcde")
        left = [
            {
                "text": text,
                "start": 119.0 + index * 0.15,
                "end": 119.05 + index * 0.15,
            }
            for index, text in enumerate(texts)
        ]
        right = [
            {
                "text": text,
                "start": 119.02 + index * 0.15,
                "end": 119.07 + index * 0.15,
            }
            for index, text in enumerate(texts)
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=119.5,
            shared_start=118.5,
            shared_end=120.5,
        )

        self.assertEqual(record["strategy"], "exact-time-anchor")
        self.assertEqual(record["anchor_run_characters"], len(texts))
        self.assertLessEqual(record["anchor_run_max_pair_delta_seconds"], 0.02)

    def test_match_run_dominance_does_not_cascade_or_drop_longer_weak_runs(
        self,
    ) -> None:
        first = ([(0, 0), (1, 1), (2, 2)], 3, 0.30)
        bridge = ([(2, 3), (3, 4), (4, 5), (5, 6)], 4, 0.20)
        last = ([(5, 7), (6, 8), (7, 9), (8, 10), (9, 11)], 5, 0.10)

        retained = cuda_worker._drop_strictly_dominated_match_runs(
            [first, bridge, last]
        )

        self.assertEqual(retained, [first, bridge, last])

    def test_dominance_discards_loose_repeated_phrase_contained_by_long_run(
        self,
    ) -> None:
        strong = ([(572 + offset, offset) for offset in range(53)], 53, 0.04)
        swapped_first = (
            [(611 + offset, 45 + offset) for offset in range(5)],
            5,
            0.92,
        )
        swapped_second = (
            [(617 + offset, 39 + offset) for offset in range(5)],
            5,
            1.0,
        )

        retained = cuda_worker._drop_strictly_dominated_match_runs(
            [strong, swapped_first, swapped_second]
        )

        self.assertEqual(retained, [strong])

    def test_dominance_accepts_observed_bounded_drift_for_a_contained_phrase(
        self,
    ) -> None:
        strong = ([(487 + offset, 149 + offset) for offset in range(26)], 26, 0.32)
        swapped_first = (
            [(504 + offset, 169 + offset) for offset in range(3)],
            3,
            0.68,
        )
        swapped_second = (
            [(507 + offset, 166 + offset) for offset in range(3)],
            3,
            0.68,
        )

        retained = cuda_worker._drop_strictly_dominated_match_runs(
            [strong, swapped_first, swapped_second]
        )

        self.assertEqual(retained, [strong])

    def test_dominance_requires_a_material_timing_advantage_and_containment(
        self,
    ) -> None:
        strong_run = [(index, index) for index in range(8)]
        contained_run = [(2 + index, 2 + index) for index in range(3)]
        outside_run = [(2 + index, 7 + index) for index in range(3)]

        cases = [
            ((strong_run, 8, 0.399), (contained_run, 3, 0.401)),
            ((strong_run, 8, 0.10), (contained_run, 3, 0.40)),
            ((strong_run, 8, 0.401), (contained_run, 3, 0.80)),
            ((strong_run, 8, 0.10), (outside_run, 3, 0.80)),
        ]
        for strong, alternative in cases:
            with self.subTest(strong=strong, alternative=alternative):
                retained = cuda_worker._drop_strictly_dominated_match_runs(
                    [strong, alternative]
                )
                self.assertEqual(retained, [strong, alternative])

    def test_shorter_but_tighter_match_run_is_not_dominated(self) -> None:
        shorter = ([(0, 0), (1, 1), (2, 2)], 3, 0.04)
        longer = ([(0, 0), (1, 1), (2, 2), (3, 3)], 4, 0.08)

        retained = cuda_worker._drop_strictly_dominated_match_runs(
            [shorter, longer]
        )

        self.assertEqual(retained, [shorter, longer])
        with self.assertRaisesRegex(ValueError, "ambiguous exact alignment"):
            cuda_worker._validate_unique_monotonic_match_runs(
                [run for run, _, _ in retained]
            )

    def test_repairs_only_a_two_character_edge_reuse_across_the_seam(self) -> None:
        weak_text = [chr(0x4E00 + index) for index in range(11)] + ["甲", "乙"]
        strong_tail = [chr(0x5000 + index) for index in range(27)]
        strong_text = ["甲", "乙", *strong_tail]
        left_text = [*weak_text, *strong_text]
        right_text = [*weak_text, *strong_tail]

        weak_left_midpoints = [115.0 + index * 0.3 for index in range(13)]
        weak_right_midpoints = [value + 0.04 for value in weak_left_midpoints]
        strong_left_midpoints = [
            118.5,
            118.8,
            *(119.0 + index * 0.12 for index in range(27)),
        ]
        left_midpoints = [*weak_left_midpoints, *strong_left_midpoints]
        right_midpoints = [
            *weak_right_midpoints,
            *(value + 0.08 for value in strong_left_midpoints[2:]),
        ]

        def items(texts: list[str], midpoints: list[float]) -> list[dict[str, object]]:
            return [
                {"text": text, "start": midpoint - 0.02, "end": midpoint + 0.02}
                for text, midpoint in zip(texts, midpoints, strict=True)
            ]

        left = items(left_text, left_midpoints)
        right = items(right_text, right_midpoints)
        left_stop, right_start, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=114.0,
            shared_end=123.0,
        )

        self.assertEqual(record["strategy"], "exact-time-anchor")
        self.assertEqual(record["anchor_run_characters"], 27)
        self.assertEqual(
            "".join(str(item["text"]) for item in left[:left_stop])
            + "".join(str(item["text"]) for item in right[right_start:]),
            "".join(left_text),
        )

    def test_edge_reuse_repair_rejects_three_characters_or_loose_timing(self) -> None:
        def overlap_items(count: int) -> list[tuple[int, dict[str, object]]]:
            return [
                (
                    index,
                    {
                        "text": chr(0x5200 + index),
                        "start": 117.0 + index * 0.1,
                        "end": 117.04 + index * 0.1,
                    },
                )
                for index in range(count)
            ]

        left_items = overlap_items(50)
        right_items = overlap_items(50)
        weak_run = [(index, index) for index in range(13)]
        three_character_reuse = [
            (13 + offset, 10 + offset) for offset in range(30)
        ]
        three_character_runs = [
            (weak_run, 13, 0.04),
            (three_character_reuse, 30, 0.20),
        ]
        self.assertEqual(
            cuda_worker._repair_edge_reuse_match_runs(
                three_character_runs,
                left_items,
                right_items,
                seam_seconds=120.0,
            ),
            three_character_runs,
        )

        two_character_reuse = [
            (13 + offset, 11 + offset) for offset in range(29)
        ]
        loose_runs = [
            (weak_run, 13, 0.04),
            (two_character_reuse, 29, 0.251),
        ]
        loose_right_items = copy.deepcopy(right_items)
        for _, item in loose_right_items[13:]:
            item["start"] = float(item["start"]) - 0.051
            item["end"] = float(item["end"]) - 0.051
        self.assertEqual(
            cuda_worker._repair_edge_reuse_match_runs(
                loose_runs,
                left_items,
                loose_right_items,
                seam_seconds=120.0,
            ),
            loose_runs,
        )

    def test_edge_reuse_repair_rejects_crossing_or_nonspanning_evidence(self) -> None:
        def overlap_items(count: int) -> list[tuple[int, dict[str, object]]]:
            return [
                (
                    index,
                    {
                        "text": chr(0x5300 + index),
                        "start": 117.0 + index * 0.1,
                        "end": 117.04 + index * 0.1,
                    },
                )
                for index in range(count)
            ]

        left_items = overlap_items(50)
        right_items = overlap_items(50)
        weak_run = [(index, index) for index in range(13)]
        crossing_run = [(10 + offset, 13 + offset) for offset in range(29)]
        crossing_runs = [
            (weak_run, 13, 0.04),
            (crossing_run, 29, 0.20),
        ]
        self.assertEqual(
            cuda_worker._repair_edge_reuse_match_runs(
                crossing_runs,
                left_items,
                right_items,
                seam_seconds=120.0,
            ),
            crossing_runs,
        )

        edge_reuse_run = [(13 + offset, 11 + offset) for offset in range(29)]
        nonspanning_runs = [
            (weak_run, 13, 0.04),
            (edge_reuse_run, 29, 0.20),
        ]
        self.assertEqual(
            cuda_worker._repair_edge_reuse_match_runs(
                nonspanning_runs,
                left_items,
                right_items,
                seam_seconds=125.0,
            ),
            nonspanning_runs,
        )

    def test_edge_reuse_repair_accepts_the_symmetric_after_seam_suffix(self) -> None:
        def overlap_items(count: int) -> list[tuple[int, dict[str, object]]]:
            return [
                (
                    index,
                    {
                        "text": chr(0x5400 + index),
                        "start": 117.0 + index * 0.1,
                        "end": 117.04 + index * 0.1,
                    },
                )
                for index in range(count)
            ]

        left_items = overlap_items(45)
        right_items = overlap_items(45)
        strong_run = [(index, index) for index in range(29)]
        after_seam_weak_run = [
            (27 + offset, 27 + offset) for offset in range(13)
        ]
        runs = [
            (strong_run, 29, 0.20),
            (after_seam_weak_run, 13, 0.04),
        ]

        repaired = cuda_worker._repair_edge_reuse_match_runs(
            runs,
            left_items,
            right_items,
            seam_seconds=119.4,
        )

        self.assertEqual(repaired[0][0], strong_run[:-2])
        self.assertEqual(repaired[0][1], 27)
        self.assertEqual(repaired[1], runs[1])

    def test_edge_reuse_repair_matches_the_observed_one_sided_suffix(self) -> None:
        def item(text: str, midpoint: float) -> dict[str, object]:
            return {
                "text": text,
                "start": midpoint - 0.02,
                "end": midpoint + 0.02,
            }

        left_midpoints = [117.0 + index * 0.12 for index in range(22)] + [
            120.28,
            120.40,
            120.52,
            120.64,
        ]
        right_midpoints = [
            *(117.2 + index * 0.12 for index in range(22)),
            119.84,
            119.96,
            120.08,
        ]
        left_items = [
            (index, item(chr(0x5500 + index), midpoint))
            for index, midpoint in enumerate(left_midpoints)
        ]
        right_items = [
            (index, item(chr(0x5600 + index), midpoint))
            for index, midpoint in enumerate(right_midpoints)
        ]
        strong_run = [(index, index) for index in range(22)]
        weak_run = [(22 + offset, 21 + offset) for offset in range(4)]
        runs = [(strong_run, 22, 0.20), (weak_run, 4, 0.56)]

        repaired = cuda_worker._repair_edge_reuse_match_runs(
            runs,
            left_items,
            right_items,
            seam_seconds=119.0,
        )

        self.assertEqual(repaired[0][0], strong_run[:-1])
        self.assertEqual(repaired[0][1], 21)
        self.assertEqual(repaired[1], runs[1])

    def test_accepts_one_unique_tightly_aligned_two_character_run(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 119.08, "end": 119.18},
            {"text": "b", "start": 119.18, "end": 119.28},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        _, _, record = cuda_worker.seam_crossover(
            left,
            right,
            seam_seconds=120.0,
            shared_start=115.0,
            shared_end=125.0,
        )

        self.assertEqual(record["anchor_run_characters"], 2)
        self.assertEqual(
            record["anchor_confidence"],
            "unique-tight-two-character-run",
        )
        self.assertAlmostEqual(
            record["anchor_run_max_pair_delta_seconds"],
            0.08,
        )

    def test_rejects_an_ambiguous_tightly_aligned_two_character_run(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 118.85, "end": 118.95},
            {"text": "b", "start": 118.95, "end": 119.05},
            {"text": "a", "start": 119.15, "end": 119.25},
            {"text": "b", "start": 119.25, "end": 119.35},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=125.0,
            )

    def test_rejects_a_two_character_run_outside_the_strict_time_gate(self) -> None:
        left = [
            {"text": "a", "start": 119.0, "end": 119.1},
            {"text": "b", "start": 119.1, "end": 119.2},
            {"text": "x", "start": 119.8, "end": 120.2},
        ]
        right = [
            {"text": "a", "start": 119.251, "end": 119.351},
            {"text": "b", "start": 119.351, "end": 119.451},
            {"text": "y", "start": 119.8, "end": 120.2},
        ]

        with self.assertRaisesRegex(ValueError, "no reliable exact"):
            cuda_worker.seam_crossover(
                left,
                right,
                seam_seconds=120.0,
                shared_start=115.0,
                shared_end=125.0,
            )

    def test_maps_owned_items_back_to_original_punctuation(self) -> None:
        text = "前句。圣安东尼奥，下一句。"
        items = [
            {"text": character, "start_time": index, "end_time": index + 0.5}
            for index, character in enumerate("前句圣安东尼奥下一句")
        ]
        self.assertEqual(
            cuda_worker.text_for_alignment_slice(
                text,
                items,
                start_item=2,
                stop_item=7,
            ),
            "圣安东尼奥，",
        )

    def test_flags_sparse_text_and_a_long_unfinished_active_tail(self) -> None:
        suspicions = cuda_worker.alignment_coverage_suspicions(
            ownership_start=3240.0,
            ownership_end=3360.0,
            text="这段只有很少的识别文字",
            alignment=[{"text": "字", "start": 3240.48, "end": 3243.92}],
            is_first_chunk=False,
            is_last_chunk=False,
        )

        self.assertEqual(
            [suspicion["kind"] for suspicion in suspicions],
            ["sparse-text", "active-trailing-gap"],
        )

    def test_terminal_punctuation_does_not_exempt_an_uncovered_tail(self) -> None:
        moderate = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text="这是一段足够长的完整句子。" * 6,
            alignment=[{"text": "句", "start": 0.0, "end": 98.0}],
            is_first_chunk=True,
            is_last_chunk=False,
        )
        severe = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text="这是一段足够长的完整句子。" * 6,
            alignment=[{"text": "句", "start": 0.0, "end": 80.0}],
            is_first_chunk=True,
            is_last_chunk=False,
        )

        self.assertTrue(any(item["kind"] == "active-trailing-gap" for item in moderate))
        self.assertTrue(any(item["kind"] == "active-trailing-gap" for item in severe))

    def test_flags_first_internal_and_final_forty_second_gaps(self) -> None:
        dense_text = "recognized speech words " * 8
        leading = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text=dense_text,
            alignment=[{"text": "word", "start": 40.0, "end": 120.0}],
            is_first_chunk=True,
            is_last_chunk=False,
        )
        internal = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text=dense_text,
            alignment=[
                {"text": "before", "start": 0.0, "end": 30.0},
                {"text": "after", "start": 70.0, "end": 120.0},
            ],
            is_first_chunk=True,
            is_last_chunk=False,
        )
        trailing = cuda_worker.alignment_coverage_suspicions(
            ownership_start=0.0,
            ownership_end=120.0,
            text=f"{dense_text}.",
            alignment=[{"text": "word", "start": 0.0, "end": 80.0}],
            is_first_chunk=True,
            is_last_chunk=True,
        )

        self.assertEqual([item["kind"] for item in leading], ["active-leading-gap"])
        self.assertEqual([item["kind"] for item in internal], ["active-internal-gap"])
        self.assertEqual([item["kind"] for item in trailing], ["active-trailing-gap"])

    def test_flags_internal_leading_gaps_and_sparse_final_chunks(self) -> None:
        leading = cuda_worker.alignment_coverage_suspicions(
            ownership_start=120.0,
            ownership_end=240.0,
            text="这是一段持续说话而且足够长的识别文字" * 8,
            alignment=[{"text": "这", "start": 140.0, "end": 220.0}],
            is_first_chunk=False,
            is_last_chunk=False,
        )
        sparse_final = cuda_worker.alignment_coverage_suspicions(
            ownership_start=240.0,
            ownership_end=360.0,
            text="太短",
            alignment=[{"text": "短", "start": 240.0, "end": 244.0}],
            is_first_chunk=False,
            is_last_chunk=True,
        )

        self.assertTrue(any(item["kind"] == "active-leading-gap" for item in leading))
        self.assertTrue(any(item["kind"] == "sparse-text" for item in sparse_final))

    def test_coverage_ignores_items_that_only_touch_core_boundaries(self) -> None:
        suspicions = cuda_worker.alignment_coverage_suspicions(
            ownership_start=120.0,
            ownership_end=240.0,
            text="这是一段持续说话而且足够长的识别文字。" * 8,
            alignment=[
                {"text": "前", "start": 119.0, "end": 120.0},
                {"text": "中", "start": 140.0, "end": 200.0},
                {"text": "后", "start": 240.0, "end": 241.0},
            ],
            is_first_chunk=False,
            is_last_chunk=False,
        )

        kinds = {item["kind"] for item in suspicions}
        self.assertIn("active-leading-gap", kinds)
        self.assertIn("active-trailing-gap", kinds)

    def test_aligned_gap_requires_quiet_audio_across_the_gap(self) -> None:
        seam = {
            "strategy": "aligned-gap",
            "seam_seconds": 120.0,
            "gap_start_seconds": 119.0,
            "gap_end_seconds": 121.0,
        }
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.0, 0.0)),
        ):
            quiet = [copy.deepcopy(seam)]
            cuda_worker.enforce_aligned_gap_silence(
                input_path=Path("source.m4a"),
                seam_records=quiet,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )
        self.assertEqual(quiet[0]["acoustic_guard"]["status"], "verified")

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "contains_low_energy_window", return_value=True),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.5, 0.3)),
        ):
            with self.assertRaisesRegex(ValueError, "not acoustically quiet"):
                cuda_worker.enforce_aligned_gap_silence(
                    input_path=Path("source.m4a"),
                    seam_records=[copy.deepcopy(seam)],
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

    def test_coverage_guard_only_rejects_sustained_active_audio(self) -> None:
        chunks = [
            {
                "start": 0.0,
                "end": 120.0,
                "text": "太短",
                "alignment": [{"text": "短", "start": 0.0, "end": 4.0}],
            },
            {
                "start": 120.0,
                "end": 121.0,
                "text": "结尾",
                "alignment": [{"text": "结", "start": 120.0, "end": 121.0}],
            },
        ]
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(cuda_worker, "active_audio_statistics", return_value=(0.0, 0.0)),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=chunks,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(116.0, 0.99),
            ),
        ):
            with self.assertRaisesRegex(ValueError, "active-audio-coverage-v1"):
                cuda_worker.enforce_alignment_coverage(
                    input_path=Path("source.m4a"),
                    chunks=chunks,
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

    def test_coverage_uses_global_owned_alignment_union_across_cores(self) -> None:
        chunks = [
            {
                "start": 2880.0,
                "end": 3000.0,
                "text": "",
                "alignment": [
                    {
                        "text": "a" * 60,
                        "start": 2880.0,
                        "end": 2974.72,
                    }
                ],
            },
            {
                "start": 3000.0,
                "end": 3120.0,
                "text": "",
                "alignment": [
                    {
                        "text": "b" * 60,
                        "start": 2975.44,
                        "end": 3120.0,
                    }
                ],
            },
        ]
        with patch.object(
            cuda_worker,
            "decode_audio_chunk",
            side_effect=AssertionError("global coverage should require no probe"),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=chunks,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

    def test_coverage_probes_first_internal_and_final_gaps(self) -> None:
        dense_text = "recognized speech words " * 8
        cases = [
            (
                "active-leading-gap",
                {
                    "start": 0.0,
                    "end": 120.0,
                    "text": dense_text,
                    "alignment": [
                        {"text": dense_text, "start": 40.0, "end": 120.0}
                    ],
                },
            ),
            (
                "active-internal-gap",
                {
                    "start": 0.0,
                    "end": 120.0,
                    "text": dense_text,
                    "alignment": [
                        {"text": dense_text, "start": 0.0, "end": 30.0},
                        {"text": dense_text, "start": 70.0, "end": 120.0},
                    ],
                },
            ),
            (
                "active-trailing-gap",
                {
                    "start": 0.0,
                    "end": 120.0,
                    "text": f"{dense_text}.",
                    "alignment": [
                        {"text": dense_text, "start": 0.0, "end": 80.0}
                    ],
                },
            ),
        ]
        for expected_kind, chunk in cases:
            with self.subTest(expected_kind=expected_kind, audio="active"):
                with (
                    patch.object(
                        cuda_worker,
                        "decode_audio_chunk",
                        return_value=FakeAudio(),
                    ),
                    patch.object(
                        cuda_worker,
                        "active_audio_statistics",
                        return_value=(40.0, 0.99),
                    ),
                ):
                    with self.assertRaisesRegex(ValueError, expected_kind):
                        cuda_worker.enforce_alignment_coverage(
                            input_path=Path("source.m4a"),
                            chunks=[chunk],
                            ffmpeg="ffmpeg",
                            numpy_module=object(),
                        )

            with self.subTest(expected_kind=expected_kind, audio="quiet"):
                with (
                    patch.object(
                        cuda_worker,
                        "decode_audio_chunk",
                        return_value=FakeAudio(),
                    ) as decode,
                    patch.object(
                        cuda_worker,
                        "active_audio_statistics",
                        return_value=(0.0, 0.0),
                    ),
                ):
                    cuda_worker.enforce_alignment_coverage(
                        input_path=Path("source.m4a"),
                        chunks=[chunk],
                        ffmpeg="ffmpeg",
                        numpy_module=object(),
                    )
                decode.assert_called_once()

    def test_short_final_tail_is_probed_without_rejecting_quiet_outro(self) -> None:
        truncated = [
            {
                "start": 0.0,
                "end": 49.85,
                "text": "unfinished",
                "alignment": [{"text": "unfinished", "start": 0.0, "end": 10.0}],
            }
        ]
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(39.85, 0.99),
            ),
        ):
            with self.assertRaisesRegex(ValueError, "active-trailing-gap"):
                cuda_worker.enforce_alignment_coverage(
                    input_path=Path("source.m4a"),
                    chunks=truncated,
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.0, 0.0),
            ),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=truncated,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )

        completed_before_outro = copy.deepcopy(truncated)
        completed_before_outro[0]["text"] = "Finished."
        with (
            patch.object(
                cuda_worker,
                "decode_audio_chunk",
                return_value=FakeAudio(),
            ) as decode,
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.0, 0.0),
            ),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=completed_before_outro,
                ffmpeg="ffmpeg",
                numpy_module=object(),
            )
        decode.assert_called_once()

    def test_explicit_final_outro_exemption_allows_only_a_bounded_final_tail(
        self,
    ) -> None:
        final_chunk = {
            "start": 0.0,
            "end": 50.0,
            "text": "finished",
            "alignment": [
                {"text": "a" * 30, "start": 0.0, "end": 33.0}
            ],
        }
        with (
            patch.object(cuda_worker, "decode_audio_chunk", return_value=FakeAudio()),
            patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(17.0, 0.99),
            ),
        ):
            with self.assertRaisesRegex(ValueError, "active-trailing-gap"):
                cuda_worker.enforce_alignment_coverage(
                    input_path=Path("source.m4a"),
                    chunks=[final_chunk],
                    ffmpeg="ffmpeg",
                    numpy_module=object(),
                )

        with patch.object(
            cuda_worker,
            "decode_audio_chunk",
            side_effect=AssertionError("verified final outro must not be probed"),
        ):
            cuda_worker.enforce_alignment_coverage(
                input_path=Path("source.m4a"),
                chunks=[final_chunk],
                ffmpeg="ffmpeg",
                numpy_module=object(),
                final_outro_exemption_seconds=17.0,
            )

    def test_final_outro_exemption_does_not_allow_internal_or_nonfinal_gaps(
        self,
    ) -> None:
        cases = [
            [
                {
                    "start": 0.0,
                    "end": 50.0,
                    "text": "first",
                    "alignment": [
                        {"text": "a" * 30, "start": 0.0, "end": 33.0}
                    ],
                },
                {
                    "start": 50.0,
                    "end": 100.0,
                    "text": "last",
                    "alignment": [
                        {"text": "b" * 30, "start": 50.0, "end": 100.0}
                    ],
                },
            ],
            [
                {
                    "start": 0.0,
                    "end": 50.0,
                    "text": "internal",
                    "alignment": [
                        {"text": "a" * 20, "start": 0.0, "end": 10.0},
                        {"text": "b" * 20, "start": 27.0, "end": 50.0},
                    ],
                }
            ],
        ]
        for chunks in cases:
            with self.subTest(chunks=len(chunks)):
                with (
                    patch.object(
                        cuda_worker,
                        "decode_audio_chunk",
                        return_value=FakeAudio(),
                    ),
                    patch.object(
                        cuda_worker,
                        "active_audio_statistics",
                        return_value=(17.0, 0.99),
                    ),
                ):
                    with self.assertRaisesRegex(ValueError, "active-"):
                        cuda_worker.enforce_alignment_coverage(
                            input_path=Path("source.m4a"),
                            chunks=chunks,
                            ffmpeg="ffmpeg",
                            numpy_module=object(),
                            final_outro_exemption_seconds=30.0,
                        )

    def test_joins_space_delimited_languages_without_merging_words(self) -> None:
        self.assertEqual(
            cuda_worker.join_transcript_chunks(
                ["first chunk", "", "second chunk"],
                language="English",
            ),
            "first chunk second chunk",
        )
        self.assertEqual(
            cuda_worker.join_transcript_chunks(
                ["第一段", "第二段"],
                language="Chinese",
            ),
            "第一段第二段",
        )

    def test_segments_a_sentence_once_across_reconciled_chunk_ownership(self) -> None:
        text = "它离呃上海火车站非常的近。"
        items = [
            {
                "text": character,
                "start_time": 119.0 + index * 0.2,
                "end_time": 119.1 + index * 0.2,
            }
            for index, character in enumerate("它离呃上海火车站非常的近")
        ]
        segments = cuda_worker.transformers_sentence_segments(
            text=text,
            aligned_items=items,
            offset_seconds=0.0,
            chunk_id=0,
            first_segment_id=0,
            max_characters=160,
            item_source_chunk_ids=[0, 0, *([1] * (len(items) - 2))],
        )

        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0]["text"], text)
        self.assertEqual(segments[0]["source_chunk_id"], 0)

    def test_rejects_non_monotonic_global_sentence_alignment(self) -> None:
        with self.assertRaisesRegex(ValueError, "globally monotonic"):
            cuda_worker.transformers_sentence_segments(
                text="AB",
                aligned_items=[
                    {"text": "A", "start_time": 1.0, "end_time": 1.2},
                    {"text": "B", "start_time": 0.9, "end_time": 1.1},
                ],
                offset_seconds=0.0,
                chunk_id=0,
                first_segment_id=0,
                max_characters=160,
            )

    def test_detects_same_size_input_mutation_during_processing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.m4a"
            path.write_bytes(b"original")
            digest = sha256_file(path)
            path.write_bytes(b"modified")

            with self.assertRaisesRegex(ValueError, "SHA-256 changed"):
                cuda_worker.validate_file_identity(
                    path,
                    expected_size_bytes=8,
                    expected_sha256=digest,
                    label="input audio",
                )

    def test_rejects_cpu_fallback_and_sampling_temperature(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = worker_args(Path(directory))
            args.device = "cpu"
            with self.assertRaisesRegex(ValueError, "explicit cuda"):
                cuda_worker.validate_arguments(args)

            args.device = "cuda:0"
            args.temperature = 0.1
            with self.assertRaisesRegex(ValueError, "temperature 0"):
                cuda_worker.validate_arguments(args)

            args.temperature = 0.0
            args.chunk_duration = float("nan")
            with self.assertRaisesRegex(ValueError, "chunk duration"):
                cuda_worker.validate_arguments(args)

            args.chunk_duration = 120.0
            args.chunk_context = float("nan")
            with self.assertRaisesRegex(ValueError, "chunk context"):
                cuda_worker.validate_arguments(args)

            args.chunk_context = 5.0
            args.chunk_duration = 181.0
            with self.assertRaisesRegex(ValueError, "both context margins"):
                cuda_worker.validate_arguments(args)

            args.chunk_duration = 120.0
            args.final_outro_exemption_seconds = float("nan")
            with self.assertRaisesRegex(ValueError, "final outro exemption"):
                cuda_worker.validate_arguments(args)

            args.final_outro_exemption_seconds = 30.001
            with self.assertRaisesRegex(ValueError, "final outro exemption"):
                cuda_worker.validate_arguments(args)

            args.final_outro_exemption_seconds = 0.0
            args.language = "Arabic"
            with self.assertRaisesRegex(ValueError, "not supported"):
                cuda_worker.validate_arguments(args)

    def test_rejects_non_finite_or_out_of_bounds_alignment(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid alignment item 0 start"):
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=float("nan"), end_time=1.0)],
                chunk_duration=2.0,
            )
        with self.assertRaisesRegex(ValueError, "exceeds its audio chunk"):
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=0.1, end_time=3.1)],
                chunk_duration=2.0,
            )

    def test_clamps_alignment_timestamp_inside_model_tolerance(self) -> None:
        self.assertEqual(
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="Test", start_time=1.9, end_time=2.2)],
                chunk_duration=2.0,
            ),
            [{"text": "Test", "start_time": 1.9, "end_time": 2.0}],
        )

    def test_clamps_observed_cuda_alignment_boundary_drift(self) -> None:
        self.assertEqual(
            cuda_worker.validate_alignment_items(
                [SimpleNamespace(text="尾", start_time=2.08, end_time=2.8)],
                chunk_duration=2.0,
            ),
            [{"text": "尾", "start_time": 2.0, "end_time": 2.0}],
        )

    def test_maps_official_tokens_after_punctuation_is_removed(self) -> None:
        segments = cuda_worker.transformers_sentence_segments(
            text="Qwen3-ASR 3.14 AI、ASR。",
            aligned_items=[
                {"text": "Qwen3ASR", "start_time": 0.1, "end_time": 0.5},
                {"text": "314", "start_time": 0.6, "end_time": 0.9},
                {"text": "AIASR", "start_time": 1.0, "end_time": 1.4},
            ],
            offset_seconds=10.0,
            chunk_id=2,
            first_segment_id=5,
            max_characters=160,
        )

        self.assertEqual(
            segments,
            [
                {
                    "id": 5,
                    "start": 10.1,
                    "end": 11.4,
                    "text": "Qwen3-ASR 3.14 AI、ASR。",
                    "source_chunk_id": 2,
                }
            ],
        )

    def test_coalesces_sentence_boundary_inside_one_official_token(self) -> None:
        segments = cuda_worker.transformers_sentence_segments(
            text="AI。ASR。",
            aligned_items=[
                {"text": "AIASR", "start_time": 0.1, "end_time": 0.8},
            ],
            offset_seconds=0.0,
            chunk_id=0,
            first_segment_id=0,
            max_characters=160,
        )

        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0]["text"], "AI。ASR。")


class ResumableWorkerTests(unittest.TestCase):
    def run_worker(
        self,
        args: argparse.Namespace,
        harness: WorkerHarness,
        *,
        duration_seconds: float = 2.0,
    ) -> int:
        def decoded_audio(*_args: object, **kwargs: object) -> FakeAudio:
            duration = float(kwargs["end_seconds"]) - float(kwargs["start_seconds"])
            return FakeAudio(round(duration * cuda_worker.SAMPLE_RATE))

        with (
            patch.object(cuda_worker, "parse_args", return_value=args),
            patch.object(cuda_worker.shutil, "which", side_effect=lambda name: name),
            patch.object(
                cuda_worker,
                "probe_audio_duration",
                return_value=duration_seconds,
            ),
            patch.object(cuda_worker, "decode_audio_chunk", side_effect=decoded_audio),
            patch.object(cuda_worker, "load_cuda_runtime", side_effect=harness.runtime),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            return cuda_worker.main()

    def test_fresh_run_writes_strict_lineage_and_uses_batch_one(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            harness = WorkerHarness()

            self.assertEqual(self.run_worker(args, harness), 0)

            raw = read_json_strict(args.output)
            aligned = read_json_strict(args.aligned_output)
            self.assertEqual(raw["engine"], "qwen-asr-transformers")
            self.assertEqual(raw["model"], cuda_worker.DEFAULT_MODEL)
            self.assertEqual(raw["options"]["backend"], "transformers")
            self.assertEqual(raw["options"]["qwen_asr_version"], "0.0.6")
            self.assertEqual(raw["options"]["torch_version"], "2.11.0")
            self.assertEqual(raw["options"]["max_inference_batch_size"], 1)
            self.assertEqual(
                raw["options"]["final_outro_exemption_seconds"], 0.0
            )
            self.assertEqual(aligned["source"]["aligner"], cuda_worker.DEFAULT_ALIGNER)
            self.assertEqual(aligned["source"]["audio_sha256"], sha256_file(args.input))
            self.assertEqual(aligned["source"]["raw_asr_sha256"], sha256_file(args.output))
            self.assertEqual(
                aligned["options"]["final_outro_exemption_seconds"], 0.0
            )
            self.assertNotIn(b"\r\n", args.output.read_bytes())
            self.assertNotIn(b"\r\n", args.aligned_output.read_bytes())

            load_asr = next(value for event, value in harness.events if event == "load-asr")
            load_aligner = next(
                value for event, value in harness.events if event == "load-aligner"
            )
            self.assertEqual(load_asr[1]["max_inference_batch_size"], 1)
            self.assertEqual(load_asr[1]["device_map"], "cuda:0")
            self.assertEqual(load_asr[1]["attn_implementation"], "sdpa")
            self.assertNotIn("max_inference_batch_size", load_aligner[1])
            self.assertEqual(harness.torch.cuda.current_device, 0)
            self.assertLess(
                next(i for i, event in enumerate(harness.events) if event[0] == "transcribe"),
                next(i for i, event in enumerate(harness.events) if event[0] == "load-aligner"),
            )

    def test_main_renders_one_sentence_across_two_reconciled_chunks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            args.language = "Chinese"
            args.chunk_duration = 2.0
            args.chunk_context = 1.0
            harness = WorkerHarness()
            events = harness.events
            transcriptions = iter(("它离呃上", "离呃上海。"))

            class MultiChunkASR:
                @classmethod
                def from_pretrained(cls, target: str, **kwargs: object) -> "MultiChunkASR":
                    events.append(("load-asr", (target, kwargs)))
                    return cls()

                def transcribe(self, **kwargs: object) -> list[SimpleNamespace]:
                    events.append(("transcribe", kwargs))
                    return [SimpleNamespace(text=next(transcriptions))]

            class MultiChunkAligner:
                @classmethod
                def from_pretrained(
                    cls, target: str, **kwargs: object
                ) -> "MultiChunkAligner":
                    events.append(("load-aligner", (target, kwargs)))
                    return cls()

                def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                    events.append(("align", kwargs))
                    if kwargs["text"] == "它离呃上":
                        values = (
                            ("它", 0.5, 0.7),
                            ("离", 1.5, 1.7),
                            ("呃", 2.0, 2.2),
                            ("上", 2.4, 2.6),
                        )
                    else:
                        values = (
                            ("离", 0.5, 0.7),
                            ("呃", 1.0, 1.2),
                            ("上", 1.4, 1.6),
                            ("海", 2.0, 2.2),
                        )
                    return [
                        [
                            SimpleNamespace(text=text, start_time=start, end_time=end)
                            for text, start, end in values
                        ]
                    ]

            harness.asr_model = MultiChunkASR
            harness.aligner = MultiChunkAligner

            self.assertEqual(
                self.run_worker(args, harness, duration_seconds=4.0),
                0,
            )

            raw = read_json_strict(args.output)
            aligned = read_json_strict(args.aligned_output)
            self.assertEqual(raw["text"], "它离呃上海。")
            self.assertEqual(len(raw["boundary_reconciliation"]["seams"]), 1)
            self.assertGreaterEqual(
                raw["boundary_reconciliation"]["seams"][0][
                    "anchor_run_characters"
                ],
                3,
            )
            self.assertEqual(len(aligned["segments"]), 1)
            self.assertEqual(aligned["segments"][0]["text"], raw["text"])
            self.assertEqual(aligned["segments"][0]["source_chunk_id"], 0)

    def test_local_snapshots_enable_offline_mode_and_are_passed_directly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            harness = WorkerHarness()

            with patch.dict(
                cuda_worker.os.environ,
                {"HF_HUB_OFFLINE": "0", "TRANSFORMERS_OFFLINE": "0"},
                clear=True,
            ):
                self.assertEqual(self.run_worker(args, harness), 0)
                self.assertEqual(cuda_worker.os.environ["HF_HUB_OFFLINE"], "1")
                self.assertEqual(cuda_worker.os.environ["TRANSFORMERS_OFFLINE"], "1")

            load_asr = next(value for event, value in harness.events if event == "load-asr")
            load_aligner = next(
                value for event, value in harness.events if event == "load-aligner"
            )
            self.assertEqual(load_asr[0], args.model_path.resolve().as_posix())
            self.assertEqual(load_aligner[0], args.aligner_path.resolve().as_posix())

    def test_complete_resume_does_not_import_cuda_or_touch_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            raw_bytes = args.output.read_bytes()
            aligned_bytes = args.aligned_output.read_bytes()

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(cuda_worker.main(), 0)

            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)

    def test_markerless_legacy_align_only_requires_retranscription(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            raw = read_json_strict(args.output)
            raw.pop("lineage_schema_version")
            raw.pop("model_identity")
            write_json_atomically(args.output, raw)
            aligned_bytes = args.aligned_output.read_bytes()

            args.aligned_output.unlink()
            raw_bytes = args.output.read_bytes()
            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                self.assertRaisesRegex(ValueError, "pass --retranscribe"),
            ):
                cuda_worker.main()
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertFalse(args.aligned_output.exists())

            args.aligned_output.write_bytes(aligned_bytes)
            args.realign = True
            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                self.assertRaisesRegex(ValueError, "pass --retranscribe"),
            ):
                cuda_worker.main()
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)

    def test_complete_markerless_legacy_chain_remains_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw.pop("lineage_schema_version")
            raw.pop("model_identity")
            write_json_atomically(args.output, raw)
            aligned = read_json_strict(args.aligned_output)
            aligned.pop("lineage_schema_version")
            aligned["source"].pop("model_identity")
            aligned["source"].pop("aligner_identity")
            aligned["source"]["raw_asr_sha256"] = sha256_file(args.output)
            write_json_atomically(args.aligned_output, aligned)
            raw_bytes = args.output.read_bytes()
            aligned_bytes = args.aligned_output.read_bytes()

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(cuda_worker.main(), 0)
            self.assertEqual(args.output.read_bytes(), raw_bytes)
            self.assertEqual(args.aligned_output.read_bytes(), aligned_bytes)

    def test_only_explicit_realign_migrates_a_legacy_final_outro_option(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            legacy_raw = read_json_strict(args.output)
            legacy_raw["options"].pop("final_outro_exemption_seconds")
            legacy_raw["options"]["boundary_reconciliation"] = (
                cuda_worker.LEGACY_BOUNDARY_RECONCILIATION_METHOD
            )
            legacy_raw["boundary_reconciliation"]["method"] = (
                cuda_worker.LEGACY_BOUNDARY_RECONCILIATION_METHOD
            )
            write_json_atomically(args.output, legacy_raw)

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
            ):
                with self.assertRaisesRegex(
                    ValueError,
                    "option final_outro_exemption_seconds mismatch",
                ):
                    cuda_worker.main()

            args.realign = True
            args.final_outro_exemption_seconds = 17.0
            harness = WorkerHarness()

            class ForbiddenASR:
                @classmethod
                def from_pretrained(cls, *args: object, **kwargs: object) -> object:
                    raise AssertionError("ASR model must not load during realign")

            harness.asr_model = ForbiddenASR
            self.assertEqual(self.run_worker(args, harness), 0)

            migrated_raw = read_json_strict(args.output)
            migrated_aligned = read_json_strict(args.aligned_output)
            self.assertEqual(
                migrated_raw["options"]["final_outro_exemption_seconds"],
                17.0,
            )
            self.assertEqual(
                migrated_raw["options"]["boundary_reconciliation"],
                cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
            )
            self.assertEqual(
                migrated_raw["boundary_reconciliation"]["method"],
                cuda_worker.BOUNDARY_RECONCILIATION_METHOD,
            )
            self.assertEqual(
                migrated_aligned["options"]["final_outro_exemption_seconds"],
                17.0,
            )
            self.assertEqual(
                migrated_aligned["source"]["raw_asr_sha256"],
                sha256_file(args.output),
            )
            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))

    def test_normal_resume_rejects_a_v2_method_without_mutating_raw(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            legacy_raw = read_json_strict(args.output)
            legacy_raw["options"]["boundary_reconciliation"] = (
                cuda_worker.LEGACY_BOUNDARY_RECONCILIATION_METHOD
            )
            legacy_raw["boundary_reconciliation"]["method"] = (
                cuda_worker.LEGACY_BOUNDARY_RECONCILIATION_METHOD
            )
            write_json_atomically(args.output, legacy_raw)
            legacy_bytes = args.output.read_bytes()

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                self.assertRaisesRegex(
                    ValueError,
                    "raw ASR decoding options do not match exactly",
                ),
            ):
                cuda_worker.main()

            self.assertEqual(args.output.read_bytes(), legacy_bytes)

    def test_explicit_realign_may_refresh_only_reconciliation_evidence(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            args.chunk_duration = 2.0
            args.chunk_context = 1.0
            def evidence_harness() -> WorkerHarness:
                harness = WorkerHarness()
                events = harness.events

                class EvidenceAligner:
                    @classmethod
                    def from_pretrained(
                        cls, target: str, **kwargs: object
                    ) -> "EvidenceAligner":
                        events.append(("load-aligner", (target, kwargs)))
                        return cls()

                    def align(
                        self, **kwargs: object
                    ) -> list[list[SimpleNamespace]]:
                        events.append(("align", kwargs))
                        return [
                            [
                                SimpleNamespace(
                                    text="Test",
                                    start_time=1.2,
                                    end_time=1.4,
                                )
                            ]
                        ]

                harness.aligner = EvidenceAligner
                return harness

            with patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.0, 0.0),
            ):
                self.assertEqual(
                    self.run_worker(
                        args,
                        evidence_harness(),
                        duration_seconds=4.0,
                    ),
                    0,
                )

            raw = read_json_strict(args.output)
            raw["boundary_reconciliation"]["seams"][0].pop(
                "anchor_run_max_pair_delta_seconds"
            )
            previous_text = raw["text"]
            previous_segments = copy.deepcopy(raw["segments"])
            write_json_atomically(args.output, raw)

            args.realign = True
            harness = evidence_harness()
            with patch.object(
                cuda_worker,
                "active_audio_statistics",
                return_value=(0.0, 0.0),
            ):
                self.assertEqual(
                    self.run_worker(args, harness, duration_seconds=4.0),
                    0,
                )

            refreshed_raw = read_json_strict(args.output)
            refreshed_aligned = read_json_strict(args.aligned_output)
            self.assertEqual(refreshed_raw["text"], previous_text)
            self.assertEqual(refreshed_raw["segments"], previous_segments)
            self.assertIn(
                "anchor_run_max_pair_delta_seconds",
                refreshed_raw["boundary_reconciliation"]["seams"][0],
            )
            self.assertEqual(
                refreshed_aligned["source"]["raw_asr_sha256"],
                sha256_file(args.output),
            )
            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))

    def test_align_only_skips_asr_model_and_reuses_valid_raw(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            args.aligned_output.unlink()

            harness = WorkerHarness()

            class ForbiddenASR:
                @classmethod
                def from_pretrained(cls, *args: object, **kwargs: object) -> object:
                    raise AssertionError("ASR model must not load during align-only")

            harness.asr_model = ForbiddenASR
            self.assertEqual(self.run_worker(args, harness), 0)
            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))
            self.assertTrue(any(event == "load-aligner" for event, _ in harness.events))

    def test_pending_raw_with_stale_aligned_self_heals_as_align_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["boundary_reconciliation"]["status"] = "pending"
            raw["boundary_reconciliation"]["seams"] = []
            for segment in raw["segments"]:
                segment["text"] = segment["decoded_text"]
                segment.pop("owned_item_start")
                segment.pop("owned_item_stop")
            raw["text"] = cuda_worker.join_transcript_chunks(
                [segment["text"] for segment in raw["segments"]],
                language=args.language,
            )
            write_json_atomically(args.output, raw)
            stale_aligned = args.aligned_output.read_bytes()

            harness = WorkerHarness()
            self.assertEqual(self.run_worker(args, harness), 0)

            self.assertFalse(any(event == "load-asr" for event, _ in harness.events))
            self.assertEqual(
                read_json_strict(args.output)["boundary_reconciliation"]["status"],
                "complete",
            )
            self.assertNotEqual(args.aligned_output.read_bytes(), stale_aligned)
            self.assertEqual(
                read_json_strict(args.aligned_output)["source"]["raw_asr_sha256"],
                sha256_file(args.output),
            )

    def test_pending_raw_modified_during_alignment_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["boundary_reconciliation"]["status"] = "pending"
            raw["boundary_reconciliation"]["seams"] = []
            for segment in raw["segments"]:
                segment["text"] = segment["decoded_text"]
                segment.pop("owned_item_start")
                segment.pop("owned_item_stop")
            raw["text"] = cuda_worker.join_transcript_chunks(
                [segment["text"] for segment in raw["segments"]],
                language=args.language,
            )
            write_json_atomically(args.output, raw)
            stale_aligned = args.aligned_output.read_bytes()

            harness = WorkerHarness()
            base_aligner = harness.aligner

            class ConcurrentRawMutationAligner(base_aligner):
                def align(self, **kwargs: object) -> list[list[SimpleNamespace]]:
                    concurrently_changed = read_json_strict(args.output)
                    concurrently_changed["generated_at"] = "concurrent-change"
                    write_json_atomically(args.output, concurrently_changed)
                    return super().align(**kwargs)

            harness.aligner = ConcurrentRawMutationAligner
            with self.assertRaisesRegex(
                ValueError, "raw ASR changed while forced alignment was running"
            ):
                self.run_worker(args, harness)

            self.assertEqual(
                read_json_strict(args.output)["generated_at"],
                "concurrent-change",
            )
            self.assertEqual(args.aligned_output.read_bytes(), stale_aligned)

    def test_changed_audio_is_rejected_before_cuda_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)
            args.input.write_bytes(b"evil-audio")

            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                with self.assertRaisesRegex(ValueError, "SHA-256"):
                    cuda_worker.main()

    def test_resume_rejects_extra_backend_option_and_wrong_raw_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["options"]["untracked_semantic_option"] = True
            write_json_atomically(args.output, raw)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "do not match exactly"):
                    cuda_worker.main()

            raw["options"].pop("untracked_semantic_option")
            write_json_atomically(args.output, raw)
            aligned = read_json_strict(args.aligned_output)
            aligned["source"]["raw_asr_sha256"] = sha256_file(args.output)
            aligned["source"]["raw_asr_path"] = "other/raw.json"
            write_json_atomically(args.aligned_output, aligned)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "raw artifact path"):
                    cuda_worker.main()

    def test_tampered_decode_window_is_rejected_before_cuda_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            raw = read_json_strict(args.output)
            raw["segments"][0]["decode_end"] = 999.0
            write_json_atomically(args.output, raw)
            with (
                patch.object(cuda_worker, "parse_args", return_value=args),
                patch.object(
                    cuda_worker,
                    "load_cuda_runtime",
                    side_effect=AssertionError("CUDA must not load"),
                ),
            ):
                with self.assertRaisesRegex(ValueError, "invalid ownership"):
                    cuda_worker.main()

    def test_negative_duration_owned_alignment_is_rejected_on_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = worker_args(root)
            args.input.write_bytes(b"fake-audio")
            self.assertEqual(self.run_worker(args, WorkerHarness()), 0)

            aligned = read_json_strict(args.aligned_output)
            aligned["chunks"][0]["alignment"][0]["end"] = 0.0
            write_json_atomically(args.aligned_output, aligned)
            with patch.object(cuda_worker, "parse_args", return_value=args):
                with self.assertRaisesRegex(ValueError, "invalid owned timestamps"):
                    cuda_worker.main()


if __name__ == "__main__":
    unittest.main()
