# Guia de uso

## 1. Configurar MCP
El archivo `.vscode/mcp.json` ya incluye el servidor `github-bbva` y los toolsets suministrados. La autenticacion debe estar disponible en tu entorno de GitHub Copilot/IDE.

## 2. Seleccionar agente
Selecciona `.github/agents/pr-merge-readiness.agent.md`.

## 3. Prompt real
`Valida el PR <URL o owner/repo#numero>. Usa github-bbva MCP. Verifica titulo, descripcion, branch develop, draft, mergeability, checks, approvals, review threads y bloqueos de seguridad disponibles. Dime si esta listo para merge. No modifiques el PR.`

## 4. Demo local sin GitHub
Ejecuta:

`python scripts/validate_pr.py demo_pr_validation/pr-ready.json`

Debe terminar en `READY TO MERGE`.

Para un escenario bloqueado:

`python scripts/validate_pr.py demo_pr_validation/pr-blocked.json`

Debe terminar en `NOT READY TO MERGE`.

## 5. Politica
Consulta `references/pr-policy.md` para modificar expresiones regulares o criterios del gate de forma centralizada.
