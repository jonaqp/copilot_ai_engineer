---
name: change-request-validation
description: Validar tickets de cambio/CRQ mediante checklist de completitud, dependencias, pruebas, ventana, rollback y aprobaciones. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Comprobar campos requeridos y consistencia.
2. Relacionar cambio con PR/commit/evidencias cuando existan.
3. Verificar plan de validación y rollback.
4. Separar bloqueantes de recomendaciones.
5. No emitir go definitivo si faltan controles obligatorios.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
