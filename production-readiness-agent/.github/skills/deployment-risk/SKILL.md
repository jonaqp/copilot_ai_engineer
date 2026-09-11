---
name: deployment-risk
description: Evaluar riesgo técnico y operativo de despliegues usando cambios de código, dependencias, historial y controles disponibles. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Identificar superficie del cambio.
2. Evaluar blast radius, criticidad y reversibilidad.
3. Considerar migraciones, contratos, feature flags y compatibilidad.
4. Asignar riesgo con razones observables, no intuición.
5. Proponer mitigaciones y señales de monitoreo.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
