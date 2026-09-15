# MCP tools esperados - Legacy / Host

## GitHub MCP oficial
Usar para leer repositorios migrados, ramas, PRs, issues, historial y ejecuciones de CI. Para diagnostico y modernizacion, configurar modo de solo lectura cuando sea suficiente.

## Host MCP corporativo (contrato propuesto, no endpoint real)
Un MCP aprobado por BBVA podria exponer herramientas de lectura como:
- `host.search_program`: localizar programa, copybook o JCL por identificador.
- `host.get_dependencies`: obtener CALL/COPY/DB2/CICS/dependencias operativas verificadas.
- `host.get_change_record`: consultar trazabilidad de cambio/paquete en la herramienta corporativa.
- `host.get_release_evidence`: recuperar evidencias previas de sincronizacion/certificacion.

No exponer desde la demo operaciones de promocion, activacion o rollback productivo. Las herramientas y nombres anteriores son un contrato de diseno; deben mapearse al MCP corporativo real aprobado.
