---
name: apx-best-practices
description: "Validar practicas APX documentadas para la demo: tipos de recursos, estructura base, modelo de ramas, pipeline, gestion de librerias y controles de calidad. Usar para comprobar cumplimiento antes de construir o desplegar."
---

# apx-best-practices

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Construir manifiesto de tipo de recurso, branch, jobs y cobertura.
2. Ejecutar `scripts/validate_apx_practices.py`.
3. Contrastar con `references/bbva_peru_rules.md`.
4. Si hay conflicto con norma vigente, prevalece la fuente oficial.

## Script ejecutable

Ejecutar `python scripts/validate_apx_practices.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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

Ejecutar un gate local compuesto:

```bash
python scripts/run_apx_quality_gate.py \
  --repo examples/apx-demo-repo \
  --manifest examples/apx_manifest.json \
  --coverage examples/jacoco.xml \
  --branch feature/DEMO-123 \
  --threshold 80
```

Compone `apx-code-review`, `apx-best-practices`, `apx-testing` y `apx-change-impact`. El resultado es evidencia local de apoyo; no reemplaza Ether/CI/Sonar/Chimera ni controles corporativos.

## Prompts de referencia

Consultar `references/prompts_es.md` para ejemplos en español orientados a BBVA Perú.
