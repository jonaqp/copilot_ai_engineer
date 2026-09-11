---
name: rollback-plan
description: Construir y validar planes de rollback/roll-forward concretos, ordenados, verificables y seguros. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Definir condición de activación.
2. Listar pasos en orden y prerequisitos.
3. Incluir responsables como roles, no personas inventadas.
4. Definir validaciones posteriores y criterios de recuperación.
5. Señalar operaciones irreversibles o pérdida potencial de datos.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
