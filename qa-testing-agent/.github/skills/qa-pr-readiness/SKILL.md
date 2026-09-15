---
name: qa-pr-readiness
description: "Validar evidencia de PR para DQA Peru: HU asociada, aprobaciones, ultima build Passed, validaciones tecnicas y vinculos a pruebas. Usar antes de enviar a QA o solicitar merge."
---

# qa-pr-readiness

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Recolectar HU, PR, aprobaciones, build y pruebas via MCP/contexto.
2. Ejecutar `scripts/validate_pr_evidence.py`.
3. Marcar bloqueantes sin asumir aplicabilidad de controles.
4. No solicitar merge si faltan aprobaciones/evidencias.

## Script ejecutable

Ejecutar `python scripts/validate_pr_evidence.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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

Generar un paquete QA completo sin publicar en Jira:

```bash
python scripts/run_qa_certification_pack.py \
  --ticket examples/qa_ticket.json \
  --xray-request examples/qa_request.json \
  --coverage examples/jacoco.xml \
  --pr-evidence examples/pr_evidence.json \
  --threshold 80
```

El wrapper utiliza `qa-ticket-jira`, `xray-generator`, `coverage-review` y `qa-pr-readiness`. Toda escritura remota queda fuera del script.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
