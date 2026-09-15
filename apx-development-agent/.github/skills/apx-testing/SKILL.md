---
name: apx-testing
description: "Revisar reportes de cobertura y exigir como baseline de APX al menos 80 por ciento sobre nuevo codigo cuando la fuente de cobertura lo permita. Usar antes de build, PR o certificacion."
---

# apx-testing

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Obtener reporte de cobertura de pipeline.
2. Ejecutar `scripts/review_apx_coverage.py --threshold 80`.
3. No confundir cobertura global con cobertura de nuevo codigo.
4. Usar el Quality Gate oficial como evidencia final.

## Script ejecutable

Ejecutar `python scripts/review_apx_coverage.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
