## What changed

<!-- Describe the user-visible or contract-level outcome. -->

## Evidence

<!-- List exact commands run and their results. Include platform-specific checks when relevant. -->

- [ ] `uv lock --check` passes when Python dependencies changed.
- [ ] Relevant Python tests and `scripts/validate.py` pass.
- [ ] `npm --prefix apps/web run check` passes for Web or content changes.
- [ ] `git diff --check` passes.

## Provenance and compatibility

- [ ] Existing source media and ASR artifacts were preserved, or replacement was explicitly requested and documented.
- [ ] New model-backed artifacts record pinned revision, resolved commit, and critical file hashes.
- [ ] Content/status claims reflect the actual review level; machine output is not marked `reviewed`.
- [ ] Any intentional migration explains how existing episodes remain readable and verifiable.

## Human review still needed

<!-- Name unresolved listening, factual, accessibility, security, or platform checks. Write "None" only when none remain. -->
