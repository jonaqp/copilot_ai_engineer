---
name: pr-metadata-validator
description: "Validate GitHub pull request title and description against the BBVA-style repository convention. Use when checking PR metadata, reviewing whether a PR follows [ISSUE-123] - PR DEVELOP and feat(ISSUE-123): description, diagnosing formatting failures, or proposing corrected metadata before merge readiness is evaluated."
---

# PR metadata validation

1. Read `../../../references/pr-policy.md` before validating.
2. Validate the title deterministically against the documented regex.
3. Validate the first non-empty description line against the documented regex.
4. Verify `base_ref=develop` when the title declares `PR DEVELOP`.
5. Report each check independently as PASS or FAIL.
6. If invalid, show the exact expected format and one corrected example; do not rewrite unrelated PR content.
7. Do not infer missing metadata. Mark it `UNKNOWN` and pass the uncertainty to the merge-readiness gate.
