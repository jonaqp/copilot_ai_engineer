# Casos de uso y prompts - QA & Testing

## Caso 1 - Pack DQA Perú

> Genera un pack QA con `qa-ticket-jira`, `xray-generator`, `coverage-review` y `qa-pr-readiness`. Usa los archivos de `examples/`. No publiques Jira/Xray; primero entrégame el payload y los bloqueantes.

## Caso 2 - Jira + GitHub MCP

> Usa GitHub MCP en lectura para obtener PR, commits y última ejecución CI. Contrástalo con la HU DQA. Si falta trazabilidad, no crees el ticket. Cuando yo confirme, usa el MCP Jira corporativo para actualizar únicamente los campos aprobados.

## Caso 3 - Xray

> Para una transferencia DataX de BBVA Perú, crea casos Xray de happy path, error de formato, reintento y reconciliación. Cada Test debe tener Test Execution y evidencias esperadas por fuente.
