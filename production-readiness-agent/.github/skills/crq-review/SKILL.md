---
name: crq-review
description: Revisar CRQs para verificar completitud, consistencia, evidencias, ventana, responsables, dependencias y criterios de éxito. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Validar campos sin completar.
2. Contrastar referencias con GitHub/MCP cuando sea posible.
3. Revisar secuencia de implementación y validación.
4. Confirmar que el rollback sea ejecutable y comprobable.
5. No modificar el CRQ sin aprobación explícita.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
