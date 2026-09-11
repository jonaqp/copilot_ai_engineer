---
name: apx-testing
description: Diseñar pruebas APX para cambios online o batch siguiendo los mecanismos de prueba presentes en el repositorio. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Detectar framework y patrones de test reales.
2. Cubrir casos nominales, límites, errores y reintentos relevantes.
3. Mockear solo fronteras externas necesarias.
4. Evitar inventar harnesses inexistentes.
5. Ejecutar pruebas y reportar cobertura cualitativa.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
