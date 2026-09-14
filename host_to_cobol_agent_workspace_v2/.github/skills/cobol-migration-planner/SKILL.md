---
name: cobol-migration-planner
description: Disenar planes incrementales de migracion HOST/Mainframe a COBOL basados en inventario y contratos de datos. Usar antes de generar codigo cuando se necesite definir alcance, orden de conversion, unidades migrables, riesgos, estrategia de pruebas y matriz de trazabilidad source-target-test.
---
# Purpose
Convertir el diagnostico en un plan verificable y de bajo riesgo.

# Workflow
1. Definir unidad migrable pequena con valor funcional.
2. Clasificar dependencias: codigo, datos, job, persistencia e integracion.
3. Separar `must preserve` de `can improve`.
4. Crear matriz `SOURCE -> TARGET -> TEST -> STATUS`.
5. Ordenar: contratos -> funciones -> I/O -> orquestacion -> job.
6. Definir rollback/convivencia si el repositorio lo permite.

Consultar `references/migration-plan-template.md`.

# Validation
No omitir contratos, entry points, codigos de retorno ni escenarios criticos descubiertos por el inventario.
