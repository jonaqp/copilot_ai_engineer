---
name: hardening-report-analysis
description: "Analizar reportes de hardening en CSV o JSON, clasificar controles fallidos por severidad y generar un backlog de remediacion. Usar cuando se recibe evidencia de hardening o compliance."
---

# hardening-report-analysis

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Obtener reporte CSV/JSON.
2. Ejecutar `scripts/analyze_hardening.py`.
3. Priorizar critical/high y validar evidencia.
4. No generar ni ejecutar scripts de cambio destructivo sin procedimiento aprobado.

## Script ejecutable

Ejecutar `python scripts/analyze_hardening.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
