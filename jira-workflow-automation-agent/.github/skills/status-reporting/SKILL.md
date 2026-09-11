---
name: status-reporting
description: Generar resúmenes ejecutivos y operativos de tickets y workflows con trazabilidad a las fuentes. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Resumir volumen, bloqueos, próximos hitos y riesgos.
2. No mezclar datos de periodos distintos sin indicarlo.
3. Citar IDs de tickets en cada afirmación importante.
4. Diferenciar hechos de interpretación.
5. Proponer próximos pasos concretos.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
