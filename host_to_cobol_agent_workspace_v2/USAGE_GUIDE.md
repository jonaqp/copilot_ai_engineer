# Guia de uso

## 1. Probar la demo sin Copilot

```bash
python scripts/inventory_host.py demo_host_migration/legacy_host
python scripts/migrate_demo.py
python scripts/run_quality_gate.py
```

La migracion escribe solo en `demo_host_migration/target_cobol/`; nunca modifica `legacy_host/`.

## 2. Probar con GitHub Copilot

Selecciona el agente `host-to-cobol-migration-engineer`.

Primer prompt:
> Analiza `demo_host_migration/legacy_host` y genera un inventario de programas, layouts, jobs, llamadas y riesgos. No migres codigo todavia.

Segundo prompt:
> Planifica la migracion de `ACCTUPD.host` a COBOL. Genera la matriz Source -> Target -> Test y marca supuestos. No cambies reglas de negocio.

Tercer prompt:
> Migra `ACCTUPD.host` a COBOL limpio en `demo_host_migration/target_cobol`, preserva `ACCOUNT.rec`, ejecuta el quality gate y reporta evidencia.

## Flujo esperado
Diagnostico -> contratos de datos -> plan -> implementacion -> validacion -> reporte.
