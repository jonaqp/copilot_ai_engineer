# MCP tools esperados - QA & Testing

## GitHub MCP oficial
Usar `repos`, `pull_requests`, `issues` y `actions` para inspeccionar codigo, PR, checks, builds y trazabilidad. Preferir lectura durante validaciones.

## Jira MCP
La configuracion `mcp/mcp.jetbrains.json` incluye Atlassian Rovo MCP **solo cuando el Jira accesible sea compatible con Atlassian Cloud y la politica corporativa lo permita**. Para Jira BBVA interno/Data Center, usar el endpoint MCP corporativo aprobado representado en `mcp/jira-bbva-internal.example.json`.

Contrato minimo deseable:
- `jira.search_issues` / `jira.get_issue`: lectura de HU, dependencias, labels y estados.
- `jira.create_issue` / `jira.update_issue`: escritura solo tras mostrar payload y obtener confirmacion humana.
- `xray.get_test`: consultar test y Test Execution.
- `xray.create_test` / `xray.create_test_execution`: publicar borradores generados por `xray-generator` solo con confirmacion.
- `xray.attach_evidence`: adjuntar evidencia ya aprobada, sin fabricar resultados.

El nombre real de cada tool depende del MCP aprobado; la Skill no debe asumirlo si el servidor no lo expone.
