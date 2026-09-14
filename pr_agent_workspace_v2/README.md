# GitHub Copilot PR Merge Readiness Agent

Workspace de ejemplo para validar Pull Requests mediante GitHub Copilot + MCP GitHub BBVA.

## Objetivo
- Recuperar evidencia real del PR via MCP.
- Validar titulo `[ISSUE-123] - PR DEVELOP`.
- Validar descripcion `feat(ISSUE-123): <descripcion>`.
- Revisar mergeabilidad, checks, aprobaciones, threads y bloqueos disponibles.
- Emitir una decision explicable: `READY TO MERGE`, `READY WITH CONDITIONS` o `NOT READY TO MERGE`.

El agente es deliberadamente read-only: nunca realiza el merge por si mismo.
