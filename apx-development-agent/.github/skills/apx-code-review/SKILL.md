---
name: apx-code-review
description: "Revisar cambios APX contra estructura del recurso, dependencias, pruebas, riesgos, Sonar/Chimera y convenciones observables en el repositorio. Usar para review previo a PR o merge."
---

# apx-code-review

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Ejecutar `scripts/review_apx_repo.py`.
2. Revisar diff y patrones APX existentes con GitHub MCP.
3. Verificar tests y evidencias Sonar/Chimera/pipeline.
4. Separar bloqueantes, warnings y normativa por confirmar.

## Script ejecutable

Ejecutar `python scripts/review_apx_repo.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
