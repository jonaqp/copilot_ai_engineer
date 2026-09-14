---
name: merge-readiness-gate
description: Produce a conservative GitHub pull request merge-readiness decision from metadata, mergeability, checks, approvals, review threads, and available security evidence. Use after PR metadata and GitHub MCP evidence have been collected to answer whether a PR is ready to merge and to enumerate exact blockers or unverifiable conditions.
---

# Merge readiness gate

1. Read `../../../references/pr-policy.md`.
2. Consume the evidence gathered by `github-mcp-pr-reader` and the metadata result from `pr-metadata-validator`.
3. Evaluate each gate independently; never hide a failed or unknown check.
4. Return exactly one final decision:
   - `READY TO MERGE`
   - `READY WITH CONDITIONS`
   - `NOT READY TO MERGE`
5. `READY TO MERGE` requires all mandatory verifiable checks to pass and no known blocker.
6. `READY WITH CONDITIONS` is only for unavailable governance/security evidence when all observed mandatory checks pass.
7. Any title, description, draft, branch, conflict, failed required check, missing required approval, unresolved-thread, or known blocking security failure yields `NOT READY TO MERGE`.
8. Provide a compact evidence table with Check, Result, Evidence/Reason.
9. End with `Merge recommendation:` followed by the decision and the next required action, if any.
10. Never execute the merge automatically.
