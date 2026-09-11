---
name: apx-development
description: Guiar desarrollo APX usando únicamente patrones, contratos y estándares observados en el repositorio o documentación autorizada. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Inspeccionar módulos similares y dependencias antes de generar código.
2. No inventar APIs APX, anotaciones o convenciones no verificadas.
3. Mantener compatibilidad hacia atrás salvo instrucción explícita.
4. Realizar cambios pequeños, revisables y trazables.
5. Ejecutar build/tests disponibles y registrar limitaciones.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
