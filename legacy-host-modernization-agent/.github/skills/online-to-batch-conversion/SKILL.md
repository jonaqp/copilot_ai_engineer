---
name: online-to-batch-conversion
description: "Evaluar si una rutina COBOL online puede convertirse o extraerse a batch, identificando acoplamientos CICS, COMMAREA, archivos, SQL y llamadas. Usar antes de proponer conversion Online a Batch."
---

# online-to-batch-conversion

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Generar inventario tecnico del programa online.
2. Ejecutar `scripts/assess_online_to_batch.py`.
3. Bloquear conversion directa si existe acoplamiento CICS/COMMAREA no resuelto.
4. Definir contrato batch, restart/recovery, idempotencia y pruebas.

## Script ejecutable

Ejecutar `python scripts/assess_online_to_batch.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
