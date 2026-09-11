# Casos de uso y prompts - Security & Hardening

## Caso 1 - Hardening

> Analiza `examples/hardening_report.csv`. Prioriza critical/high, conserva la evidencia original y genera un plan de remediación con owner, validación y rollback. No ejecutes comandos en infraestructura.

## Caso 2 - Controles BBVA Perú

> Valida `examples/security_manifest.json` con `security-control-validator`. Revisa segregación, datos productivos en previos, transporte cifrado/TLS y pipeline. Si el alcance de un control no está claro, marca pregunta para Arquitectura de Seguridad.

## Caso 3 - GitHub Code Security

> Usa GitHub MCP únicamente con toolsets de seguridad permitidos para leer findings del repo/PR. Correlaciónalos con el hardening local y separa duplicados, falsos positivos por revisar y bloqueantes de release.
