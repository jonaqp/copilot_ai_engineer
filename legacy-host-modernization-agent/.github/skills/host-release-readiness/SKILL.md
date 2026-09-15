---
name: host-release-readiness
description: "Validar un manifiesto de pase Host contra criterios DQA Peru de demo: paquetes listos para sincronizar, plan de retorno, trazabilidad Jira y evidencias. Usar antes de solicitar certificacion o release."
---

# host-release-readiness

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Completar manifiesto de release.
2. Ejecutar `scripts/validate_host_release.py`.
3. Resolver bloqueantes de plan de retorno, paquetes y trazabilidad.
4. Solicitar aprobacion humana antes de cualquier pase.

## Script ejecutable

Ejecutar `python scripts/validate_host_release.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
