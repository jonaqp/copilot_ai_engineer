---
name: frontend-quality-gate
description: Validar HTML/CSS del proyecto contra los estándares locales y accesibilidad básica. Usar antes de finalizar cambios Front-End, al revisar código generado por Copilot, o cuando el usuario pida auditoría, validación o corrección de una interfaz.
---

# Frontend Quality Gate

## Purpose
Aplicar un ciclo determinista de validación y corrección acotada.

## Inputs
- HTML/CSS modificados.
- Referencias de `reference-standards/`.

## Workflow & Instructions
1. Ejecutar `python scripts/style_validator.py --file <html>` por cada HTML afectado.
2. Si se modificaron referencias o skills, ejecutar `python scripts/workspace_check.py`.
3. Corregir únicamente los criterios que fallen.
4. Repetir como máximo 2 veces por el mismo criterio.
5. Si el error persiste, detenerse y reportar evidencia concreta.

## Expected Output
Resumen de checks: `PASS`, `WARN` o `FAIL`, con archivo y criterio.

## Validation
Finalizar solo cuando no queden `FAIL`. Los `WARN` deben explicarse si no se corrigen.
