# Uso de MCP

## GitHub MCP Server

`.vscode/mcp.json` usa la imagen oficial `ghcr.io/github/github-mcp-server` con OAuth. No guarda PATs en el repositorio.

Casos de uso: leer repositorios, commits, PRs, issues e historial para fundamentar el análisis.

Para escenarios de solo análisis, se recomienda configurar el servidor en **read-only**. Para PAT, usar secretos/variables de entorno y mínimo privilegio.

## MCP de demo local

`mcp/demo_server.py` expone dos herramientas sin datos corporativos: `get_agent_context` y `validate_change`. Sirve para practicar descubrimiento y llamadas MCP.

Config de ejemplo: `mcp/local-demo-mcp.json`. Puede fusionarse con `.vscode/mcp.json` si se desea ejecutarlo en el IDE.

## Producción

Reemplazar el MCP demo por conectores autorizados. Para Cells / Frontend Agent, la prioridad sería: github. Separar credenciales por entorno, limitar toolsets y auditar acciones de escritura.
