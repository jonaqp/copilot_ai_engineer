# Guia de uso

## 1. Configurar MCP
Abrir `.vscode/mcp.json`. El token se solicita como input seguro; no lo escribas en el repositorio.

## 2. Seleccionar agente
Seleccionar `jira-ticket-quality` en GitHub Copilot.

## 3. Primera prueba offline
Desde la raiz:

```bash
python scripts/validate_ticket.py demo_jira_ticket/ticket-ready.json
```
Debe devolver `READY`.

Caso con errores:
```bash
python scripts/validate_ticket.py demo_jira_ticket/ticket-needs-fix.json
```
Debe devolver `NOT READY`.

## 4. Lectura real via MCP
Prompt sugerido:
`Lee DEDATIOCL1-21347 usando mcp-atlassian. No escribas nada. Valida formato, descripcion, DoR/DoD/Acceptance Criteria, attachments, links y subtasks. Devuelve evidencias y readiness.`

## 5. Correccion
Primero pedir:
`Propone las correcciones necesarias sin modificar Jira.`

Luego, si son correctas:
`Aplica solo las correcciones propuestas al ticket DEDATIOCL1-21347, releelo y vuelve a validar.`

## 6. Adjuntos
Si el MCP permite descargar el binario, validar localmente. Si no, el agente debe reportar `UNKNOWN_VISUAL` en vez de afirmar que la imagen es correcta.
