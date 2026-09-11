---
name: accessibility-review
description: Evaluar accesibilidad de interfaces y componentes con checklist práctico de semántica, teclado, foco, formularios y contenido. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Revisar semántica HTML y nombres accesibles.
2. Validar navegación por teclado y orden de foco.
3. Comprobar mensajes de error, labels y estados dinámicos.
4. Evitar afirmar conformidad total sin pruebas automáticas y manuales.
5. Entregar hallazgos con impacto, evidencia y corrección sugerida.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
