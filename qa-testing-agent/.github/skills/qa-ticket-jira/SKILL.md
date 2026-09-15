---
name: qa-ticket-jira
description: "Construir y validar una HU/ticket de certificacion QA para BBVA Peru con los campos minimos de DQA, sin crearla en Jira hasta que el usuario confirme. Usar para preparar solicitudes de revision o certificacion."
---

# qa-ticket-jira

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Preparar JSON del ticket sin publicarlo.
2. Ejecutar `scripts/validate_qa_ticket.py`.
3. Corregir bloqueantes del baseline DQA.
4. Pedir confirmacion antes de usar Jira MCP para crear/actualizar.

## Script ejecutable

Ejecutar `python scripts/validate_qa_ticket.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

## Referencias

Consultar `references/bbva_peru_rules.md` antes de emitir una conclusion de cumplimiento. Si el documento interno vigente contradice esta Skill, prevalece el documento vigente.

## Salida esperada

Entregar: objetivo, entradas utilizadas, evidencia, hallazgos clasificados, riesgos, acciones propuestas, validaciones pendientes y cualquier aprobacion humana requerida.

## Guardrails

- No inventar IDs Jira, nombres de UUAA, endpoints, credenciales, APIs propietarias o resultados de pipeline.
- Diferenciar hecho observado, inferencia y dato pendiente.
- No afirmar que tests/quality gates pasaron sin evidencia de ejecucion.
- No ejecutar acciones productivas o destructivas desde esta Skill.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
