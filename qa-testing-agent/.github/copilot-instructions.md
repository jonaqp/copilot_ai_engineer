# Instrucciones de GitHub Copilot - QA & Testing Agent

- Responder en espanol salvo solicitud contraria.
- Usar primero el contexto del repositorio y las Skills de `.github/skills/`; no inventar patrones corporativos.
- Ejecutar scripts de las Skills para validaciones deterministas cuando existan.
- Tratar reglas de `references/bbva_peru_rules.md` como baseline versionable de demo; prevalece la normativa interna vigente.
- No inventar resultados de tests, Sonar, Chimera, Xray, Jira, CI/CD ni evidencias.
- No incluir secretos, tokens ni datos productivos en prompts, logs o archivos de ejemplo.
- Preferir MCP de solo lectura; pedir confirmacion humana antes de escrituras en GitHub/Jira y no ejecutar acciones productivas.
- Distinguir claramente evidencia observada, inferencia y dato pendiente.
