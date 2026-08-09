# Security policy

## Supported version

PodWiki is maintained from the `main` branch. Security fixes are applied there; historical
commits, local media caches, and generated artifacts are not maintained as separate release
lines.

## Report a vulnerability

Use the repository's **Security → Report a vulnerability** flow to open a private security
advisory. Do not publish exploit details, private source URLs, credentials, personal data, or
access-control bypasses in a public issue.

Include the affected path and revision, the minimum reproduction, impact, and any safe
mitigation you have tested. For media acquisition issues, state the public platform and source
type without attaching copyrighted media or signed temporary URLs.

A maintainer will acknowledge a complete report within seven days and will keep material
status changes in the private advisory until disclosure is coordinated. This is a
best-effort community project, so remediation timing depends on severity and maintainer
availability.

## Scope and safety boundaries

High-value reports include source-identity confusion, path traversal, unsafe overwrite or
recovery behavior, secret exposure, dependency compromise, and validation bypasses that can
publish untrusted content. The project does not accept workflows that bypass login,
membership, payment, regional, or other access controls.
