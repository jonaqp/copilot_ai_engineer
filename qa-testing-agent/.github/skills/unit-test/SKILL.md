---
name: unit-test
description: "Detectar el stack de pruebas de un repositorio, proponer o ejecutar de forma segura el comando de tests permitido y generar una ficha de resultados. Usar para crear, completar o verificar pruebas unitarias."
---

# unit-test

## Objetivo

Aplicar un flujo repetible y auditable para esta capacidad dentro de GitHub Copilot. Usar evidencia del repositorio, parametros del usuario y referencias aprobadas; no completar datos corporativos por suposicion.

## Flujo

1. Detectar stack y comando con `scripts/detect_and_run_tests.py`.
2. Generar tests siguiendo patrones existentes.
3. Ejecutar tests solo con `--run` y comandos allowlisted.
4. Reportar fallos reales; no ocultar tests preexistentes fallidos.

## Script ejecutable

Ejecutar `python scripts/detect_and_run_tests.py --help` para ver parametros. Usar el script para la parte determinista y dejar al modelo la interpretacion, priorizacion y redaccion.

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
