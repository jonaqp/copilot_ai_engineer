---
name: test-quality-gate
description: Validar una suite Python/Flask antes de finalizar cambios de testing. Usar como último paso para ejecutar pytest, verificar coverage >=80%, detectar fallos, comprobar estructura básica y producir evidencia de calidad reproducible.
---

# Test Quality Gate

## Purpose
Aplicar una validación determinista y bloquear entregas con suite fallida o coverage insuficiente.

## Inputs
- Código Python.
- Tests.
- Configuración de pytest/coverage.

## Workflow & Instructions
1. Ejecutar `python scripts/run_quality_gate.py`.
2. Si falla un test, corregir el comportamiento o test concreto; máximo 2 ciclos por el mismo fallo.
3. Si coverage <80%, ejecutar `coverage_gap_report.py` y priorizar huecos.
4. No reducir el umbral ni excluir archivos para pasar.
5. Finalizar solo con suite verde y coverage >=80%.

## Expected Output
Resumen `PASS/FAIL`, total de tests y coverage.

## Validation
- Exit code 0.
- Coverage global >=80%.
- Sin tests fallidos.
