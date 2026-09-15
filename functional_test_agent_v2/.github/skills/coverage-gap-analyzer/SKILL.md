---
name: coverage-gap-analyzer
description: Analizar reportes de coverage de Python para encontrar módulos, líneas y ramas prioritarias sin cobertura. Usar cuando el coverage esté por debajo de 80%, cuando un módulo crítico tenga baja cobertura o antes de decidir qué tests agregar para maximizar valor y no solo porcentaje.
---

# Coverage Gap Analyzer

## Purpose
Convertir el reporte de cobertura en una lista priorizada de huecos de test.

## Inputs
- `coverage.xml` o salida de `pytest --cov-report=term-missing`.
- Código relacionado con líneas faltantes.
- `.github/reference-standards/coverage-standard.md`.

## Workflow & Instructions
1. Ejecutar `python scripts/run_coverage.py`.
2. Ejecutar `python scripts/coverage_gap_report.py coverage.xml`.
3. Revisar primero archivos críticos bajo 70%.
4. Mapear líneas faltantes a comportamientos, no a líneas aisladas.
5. Priorizar errores, ramas, transiciones de estado y endpoints.
6. Ignorar solo código realmente no ejecutable o defensivo, documentando la razón.
7. Delegar la creación de tests a la skill específica.

## Expected Output
Lista ordenada de archivos/huecos con comportamiento sugerido a probar.

## Validation
El plan debe explicar por qué cada test propuesto aporta valor funcional.
