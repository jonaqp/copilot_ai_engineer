# PR Validation Policy

## Title
Required format:

`[<ISSUE_KEY>] - PR DEVELOP`

Example:

`[DEDATIOEN4-18921] - PR DEVELOP`

Default regex:

`^\[[A-Z0-9]+-[0-9]+\] - PR DEVELOP$`

Rules:
- Uppercase issue key.
- Exactly one space around `-` before `PR DEVELOP`.
- No extra prefix or suffix.
- Base branch must be `develop` when the title declares `PR DEVELOP`.

## Description
The first non-empty line must use:

`feat(<ISSUE_KEY>): <description>`

Example:

`feat(DEDATIOCL1-22769): actualiza validacion de contratos del checkout`

Default regex:

`^feat\([A-Z0-9]+-[0-9]+\): .+`

Rules:
- `<description>` must be non-empty.
- Do not require the title issue key and description issue key to be identical unless repository policy explicitly says so.
- Additional body lines are allowed after the first line.

## Merge-readiness gate
Mark `READY TO MERGE` only when all verifiable mandatory conditions pass:
1. PR is OPEN.
2. PR is not a draft.
3. Base branch is `develop`.
4. Title format passes.
5. Description format passes.
6. GitHub reports the PR as mergeable / conflict free.
7. Required checks are successful.
8. Required approvals are satisfied when the repository exposes this requirement.
9. No unresolved review threads when this information is available.
10. No blocking security/dependency finding when the MCP exposes a blocker for the PR.

Use `READY WITH CONDITIONS` when format and core merge state pass but one or more governance/security signals cannot be verified from the available MCP response.
Use `NOT READY TO MERGE` for any failed mandatory condition.

Never merge, approve, close, update, or modify a PR unless the user explicitly requests that action after reviewing the validation result.
