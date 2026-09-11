---
name: apx-change-impact
description: Analizar impacto de cambios APX sobre componentes, contratos, jobs, servicios y consumidores usando evidencia de repositorio y MCP. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Identificar archivo/componente origen y naturaleza del cambio.
2. Buscar referencias, dependencias y contratos afectados.
3. Construir lista de impactos directos e indirectos con evidencia.
4. Clasificar riesgo y pruebas de regresión recomendadas.
5. No afirmar ausencia de impacto si la búsqueda fue parcial.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
