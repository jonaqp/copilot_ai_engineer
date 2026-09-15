---
name: security-control-validator
description: "Validar un manifiesto tecnico contra controles de seguridad BBVA Peru resumidos para la demo: segregacion, datos no productivos, cifrado en transito, TLS y repositorio/pipeline. Usar durante diseno o revision tecnica."
---

# security-control-validator

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Preparar manifiesto tecnico.
2. Ejecutar `scripts/validate_security_controls.py`.
3. Contrastar gaps con Arquitectura de Seguridad vigente.
4. Registrar excepciones/aceptaciones de riesgo solo con owner autorizado.

## Script ejecutable

Ejecutar `python scripts/validate_security_controls.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
