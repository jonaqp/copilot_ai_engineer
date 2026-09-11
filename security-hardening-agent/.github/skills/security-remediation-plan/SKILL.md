---
name: security-remediation-plan
description: "Convertir findings de seguridad en un plan priorizado con responsable, accion, validacion y rollback. Usar despues del analisis; nunca ejecutar cambios de infraestructura automaticamente."
---

# security-remediation-plan

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Partir de findings validados.
2. Ejecutar `scripts/build_remediation_plan.py`.
3. Asignar owner, validacion y rollback.
4. Mantener status Proposed hasta aprobacion humana.

## Script ejecutable

Ejecutar `python scripts/build_remediation_plan.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

## Referencias

Consultar `references/bbva_peru_rules.md` antes de emitir una conclusion de cumplimiento. Si el documento interno vigente contradice esta Skill, prevalece el documento vigente.

## Salida esperada

Entregar: objetivo, entradas utilizadas, evidencia, hallazgos clasificados, riesgos, acciones propuestas, validaciones pendientes y cualquier aprobacion humana requerida.

## Guardrails

- No inventar IDs Jira, nombres de UUAA, endpoints, credenciales, APIs propietarias o resultados de pipeline.
- Diferenciar hecho observado, inferencia y dato pendiente.
- No afirmar que tests/quality gates pasaron sin evidencia de ejecucion.
- No ejecutar acciones productivas o destructivas desde esta Skill.

## Composición con otras Skills

```bash
python scripts/run_security_hardening_pack.py \
  --report examples/hardening_report.csv \
  --manifest examples/security_manifest.json \
  --pipeline examples/Jenkinsfile
```

Compone `hardening-report-analysis`, `security-control-validator`, `secure-pipeline-review` y `security-remediation-plan`. Solo genera análisis y propuesta; nunca aplica cambios sobre infraestructura.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
