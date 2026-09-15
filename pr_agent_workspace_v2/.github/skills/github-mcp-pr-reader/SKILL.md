---
name: github-mcp-pr-reader
description: Retrieve pull request evidence from the configured GitHub BBVA MCP endpoint for validation and merge-readiness analysis. Use when a PR URL, repository plus PR number, or current pull request must be inspected for title, body, state, draft status, base branch, mergeability, checks, reviews, unresolved threads, or security/dependency blockers.
---

# GitHub MCP PR reader

1. Use the configured MCP server `github-bbva` from `.vscode/mcp.json`.
2. Prefer read-only operations from the `pull_requests`, `repos`, `code_security`, and `dependabot` toolsets.
3. Discover the concrete MCP operation names exposed by the client; never invent an operation name.
4. Retrieve at minimum: repository, PR number, title, body, state, draft flag, base branch, head SHA, mergeable/merge state, status checks, review/approval state.
5. When available, retrieve unresolved review threads and blocking security/dependency findings associated with the PR or head SHA.
6. Preserve raw evidence needed for the final decision. Distinguish `PASS`, `FAIL`, and `UNKNOWN`.
7. Do not update, merge, approve, close, label, or comment on the PR during validation.
8. If authentication or a required MCP capability is unavailable, state exactly which evidence could not be retrieved.

See `../../../references/pr-policy.md` for the policy consumed by the validator.
