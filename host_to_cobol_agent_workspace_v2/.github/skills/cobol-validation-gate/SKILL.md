---
name: cobol-validation-gate
description: Validar migraciones HOST/Mainframe a COBOL con quality gates estructurales, de contratos y regresion. Usar despues de generar o modificar COBOL para verificar trazabilidad, campos, codigos de retorno, anti-patrones, escenarios de entrada/salida y compilacion cuando exista compilador, antes de aprobar la migracion.
---
# Purpose
Impedir que una migracion incompleta o semanticamente dudosa sea considerada terminada.

# Workflow
1. Validar estructura COBOL basica.
2. Detectar TODO/FIXME/placeholders y GOTO nuevo.
3. Verificar contratos y copybooks requeridos.
4. Comparar casos de regresion legacy/target cuando existan.
5. Compilar si hay compilador disponible.
6. Emitir `PASS`, `PASS WITH CONDITIONS` o `FAIL` con evidencia.

Consultar `references/quality-gate.md`.

# Validation
PASS exige cero errores bloqueantes y cero supuestos criticos sin resolver. La ausencia de compilador debe declararse como condicion.
