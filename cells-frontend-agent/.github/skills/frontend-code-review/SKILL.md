---
name: frontend-code-review
description: Revisar cambios frontend con foco en correctitud, mantenibilidad, seguridad del cliente, rendimiento y regresiones. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Leer diff y archivos relacionados antes de opinar.
2. Priorizar hallazgos por severidad y evidencia.
3. Distinguir defectos confirmados de riesgos hipotéticos.
4. Revisar manejo de errores, estados, dependencias y compatibilidad.
5. Proponer correcciones pequeñas y verificables.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
