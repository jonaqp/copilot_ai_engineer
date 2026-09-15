---
name: coverage-review
description: "Leer reportes coverage.py, JaCoCo XML o LCOV y evaluar porcentaje, archivos con brechas y umbral solicitado. Usar para revisar cobertura antes de PR o certificacion."
---

# coverage-review

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Identificar formato de coverage.
2. Ejecutar `scripts/review_coverage.py --threshold <N>`.
3. Distinguir cobertura global de new-code coverage.
4. Priorizar brechas y proponer tests concretos.

## Script ejecutable

Ejecutar `python scripts/review_coverage.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
