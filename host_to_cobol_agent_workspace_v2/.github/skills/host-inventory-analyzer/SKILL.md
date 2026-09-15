---
name: host-inventory-analyzer
description: Inventariar proyectos HOST/Mainframe antes de una migracion a COBOL. Usar cuando se necesite descubrir programas legacy, entry points, llamadas, COPY/copybooks, JCL/jobs, archivos, I/O, datos y dependencias, o cuando el agente de migracion necesite una fotografia tecnica verificable antes de planificar o generar COBOL.
---
# Purpose
Construir un inventario tecnico minimo y trazable antes de migrar.

# Inputs
- Carpeta fuente HOST/legacy.
- JCL/jobs, layouts, copybooks y configuracion disponibles.

# Workflow
1. Enumerar artefactos por tipo.
2. Detectar programas, llamadas y dependencias textuales sin inventar relaciones.
3. Extraer I/O, datasets, records y codigos de retorno observables.
4. Marcar zonas ambiguas como SUPUESTO.
5. Generar inventario Markdown/JSON cuando sea util.

Consultar `references/inventory-standard.md`. Para la demo usar `scripts/inventory_host.py` o el wrapper raiz.

# Expected Output
Programas, dependencias, contratos, hotspots y evidencia de origen.

# Validation
No declarar una dependencia como confirmada si solo es inferida. Verificar que cada artefacto reportado exista realmente.
