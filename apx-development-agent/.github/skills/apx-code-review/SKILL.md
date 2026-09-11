---
name: apx-code-review
description: Revisar cambios APX con foco en contratos, compatibilidad, manejo de errores, observabilidad, seguridad y mantenibilidad. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Leer diff, callers y callees relevantes.
2. Revisar contratos y efectos secundarios.
3. Buscar cambios incompatibles y dependencias no evidentes.
4. Priorizar hallazgos por impacto y probabilidad.
5. Proponer pruebas específicas por hallazgo.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
