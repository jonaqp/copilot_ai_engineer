---
name: frontend-testing
description: Diseñar y generar pruebas unitarias, integración y UI para cambios frontend de forma determinista y mantenible. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Identificar comportamiento observable y límites del componente.
2. Cubrir happy path, errores, estados vacíos y eventos.
3. Evitar pruebas acopladas a detalles internos innecesarios.
4. Preferir selectores y aserciones orientados al usuario.
5. Ejecutar el conjunto relevante y reportar resultados.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
