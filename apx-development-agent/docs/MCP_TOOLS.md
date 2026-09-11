# MCP tools esperados - APX Development

## GitHub MCP oficial
Usar repositorios, PRs, issues y Actions para obtener evidencia real antes de generar o revisar codigo.

## APX / Engineering MCP corporativo (contrato propuesto)
Un MCP interno aprobado puede proporcionar:
- `apx.get_resource`: tipo de recurso, runtime y metadatos de la UUAA.
- `apx.get_governance`: reglas/estado de gobierno vigentes para el componente.
- `apx.get_dependencies`: dependencias entre UD, librerias y DTOs.
- `pipeline.get_build`: ultima build y checks reales.
- `quality.get_sonar_gate`: Quality Gate observado.
- `security.get_chimera_findings`: hallazgos de seguridad observados.

Los nombres son contractuales para la demo, no APIs oficiales. Antes de conectarlos, mapearlos a los MCP corporativos reales y aprobados. No desplegar ni aprobar cambios productivos automaticamente.
