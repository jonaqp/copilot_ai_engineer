---
name: jira-ticket-authoring
description: Transformar requisitos o notas en tickets Jira completos, trazables y accionables sin inventar datos de negocio. Use when GitHub Copilot needs this repeatable capability inside the corresponding engineering workflow.
---

# Workflow

1. Extraer objetivo, alcance, contexto y dependencias.
2. Redactar descripción, criterios de aceptación y evidencias esperadas.
3. Marcar como TBD cualquier dato obligatorio no proporcionado.
4. Evitar asignar responsables, fechas o prioridades sin evidencia.
5. Preparar payload para MCP Jira solo después de revisión del usuario cuando implique escritura.

# Guardrails

- Basar conclusiones en evidencia observable del repositorio, herramientas o fuentes autorizadas.
- No inventar estándares internos, APIs, IDs, aprobaciones ni resultados de pruebas.
- Minimizar privilegios y evitar secretos en prompts, logs, commits o archivos generados.
- Separar hechos, supuestos y recomendaciones.
- Antes de acciones irreversibles o de escritura externa, exigir confirmación cuando no esté explícitamente autorizada.

# Output

Entregar una respuesta breve y trazable con: objetivo, evidencia, análisis/acción, validación y riesgos pendientes.
