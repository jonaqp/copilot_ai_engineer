# Jira MCP - BBVA Peru

Este repositorio no inventa un endpoint corporativo de Jira.

## Modo remoto homologado

1. Obtener del catalogo corporativo el endpoint MCP Jira aprobado para la geografia/BU.
2. Copiar `jira-bbva.template.jetbrains.json` o `qa-github-jira-full.template.jetbrains.json`.
3. Reemplazar `<PEGAR_ENDPOINT_MCP_JIRA_HOMOLOGADO_BBVA>`.
4. Configurar la autenticacion siguiendo el mecanismo corporativo del servidor homologado.
5. Mantener operaciones de escritura detras de confirmacion humana explicita.

El Custom Agent usa el namespace `jira-bbva/*`. Si el servidor corporativo se registra con otro nombre, ajustar el nombre del servidor o el `tools:` del `.agent.md`.

## Modo local para taller

Usar `../local/qa-github-jira-local.jetbrains.json`. El servidor `qa-local` incluye un almacen Jira sintetico en `mcp/data/jira_issues.json` y herramientas de preparacion/validacion. `jira_upsert_issue_local` solo escribe en ese JSON local y exige `confirm=true`; nunca conecta con Jira real.

> Gobernanza: antes de habilitar Jira/Xray remoto, comprobar que el MCP y sus tools estan homologados/activos en el catalogo corporativo vigente. La demo no convierte un template en una autorizacion.
