---
name: production-readiness
description: Evaluar preparación de un cambio para producción con checklist de pruebas, dependencias, aprobaciones, observabilidad y reversibilidad. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Recopilar PR, build, test, CRQ y dependencias.
2. Evaluar bloqueantes antes de recomendaciones.
3. Comprobar observabilidad y plan post-deploy.
4. Exigir rollback o roll-forward viable según criticidad.
5. Emitir Ready, Ready with conditions o Not ready con evidencia.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
