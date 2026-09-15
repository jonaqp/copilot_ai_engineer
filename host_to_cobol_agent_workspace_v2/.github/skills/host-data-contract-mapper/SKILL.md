---
name: host-data-contract-mapper
description: Mapear contratos de datos HOST/Mainframe a definiciones COBOL seguras. Usar cuando la migracion incluya records, layouts, copybooks, archivos fijos, PIC, campos numericos/alfanumericos, signos, claves o compatibilidad de registros y se necesite preservar tipos, longitudes y semantica en el COBOL destino.
---
# Purpose
Preservar contratos de datos durante la migracion.

# Workflow
1. Leer layout fuente y su uso real.
2. Registrar nombre, posicion/orden, longitud, tipo, signo y regla.
3. Proponer PIC equivalente sin alterar silenciosamente longitud/precision.
4. Separar contrato reusable en COPYBOOK cuando aplique.
5. Crear matriz Source Field -> COBOL Field -> PIC -> Validacion.

Consultar `references/data-mapping-standard.md`.

# Guardrails
No asumir encoding, packed decimal o signed format sin evidencia. No perder fillers, claves ni campos reservados si forman parte del record fisico.

# Validation
Comprobar conteo de campos, longitudes totales cuando esten definidas y mapeo de campos obligatorios.
