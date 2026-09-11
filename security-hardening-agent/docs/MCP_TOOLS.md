# MCP tools esperados - Security & Hardening

## GitHub MCP oficial
Habilitar toolsets de repositorio, PR, Actions y `code_security` cuando el plan/politica lo permitan. Leer findings; no cerrar alertas automaticamente.

## Security MCP corporativo (contrato propuesto)
Capacidades de lectura sugeridas:
- `security.get_control`: texto/version/aplicabilidad de un control vigente.
- `hardening.get_profile`: baseline de hardening aprobado para tecnologia/OS.
- `vulnerability.search_findings`: findings de escaneo y evidencias.
- `cmdb.get_asset`: contexto de activo y criticidad, si esta autorizado.
- `pipeline.get_security_checks`: resultados reales de pipeline.

Acciones de remediacion, cambios de configuracion, excepciones o cierres deben quedar fuera del MCP de demo o requerir aprobacion humana explicita y controles corporativos.
