# PyCharm + GitHub Copilot - APX Development Agent

1. Abrir esta carpeta como proyecto.
2. Activar plugin GitHub Copilot aprobado por la organización.
3. Copilot Chat -> Agent -> Configure Agents -> Workspace.
4. Seleccionar `.github/agents/apx-development.agent.md`.
5. Verificar que el modelo sea **Claude Sonnet 5** o únicamente otra opción Claude aprobada.
6. Agent -> Tools -> Add MCP Tools y copiar uno de los JSON de `mcp/remote` o `mcp/local`.
7. Ejecutar `python scripts/test_local_mcp.py` para validar el MCP de dominio sin red.

Custom Agents/Skills/MCP dependen de la versión del plugin y de las políticas Enterprise; si una capability no aparece, verificar primero versión/política y no modificar el diseño del agente por suposición.
