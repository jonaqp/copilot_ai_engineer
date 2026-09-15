---
name: jira-format-validator
description: Valida formato y contenido textual de tickets Jira BBVA contra perfiles versionados. Usar para revisar summary, description, tablas, listas, campos obligatorios, DoR, DoD, Acceptance Criteria y consistencia de cantidades antes de corregir o aprobar un ticket.
---
# Workflow
1. Cargar `../../../references/jira-ticket-standard.md` cuando el perfil sea `deployment-datax`.
2. Validar summary por componentes semanticos, no solo por longitud.
3. Validar que la descripcion tenga secciones y datos esperados.
4. Detectar placeholders vacios, N/A sin contexto, texto ambiguo y conteos inconsistentes.
5. Validar DoR, DoD y Acceptance Criteria usando evidencia real.
6. Devolver hallazgos atomicos con `rule_id`, resultado, evidencia y correccion sugerida.
7. No escribir el ticket.
