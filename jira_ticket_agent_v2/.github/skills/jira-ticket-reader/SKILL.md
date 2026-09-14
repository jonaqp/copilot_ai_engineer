---
name: jira-ticket-reader
description: Recupera un snapshot completo de un issue Jira mediante mcp-atlassian. Usar cuando el agente necesite analizar un ticket, revisar campos, descripcion, adjuntos, links, subtareas, comentarios o estados antes de validar o modificarlo.
---
# Workflow
1. Obtener el issue por key.
2. Recuperar como minimo summary, description, status, resolution, priority, assignee, reporter, labels, dates y campos de readiness disponibles.
3. Recuperar attachments con id, filename, mime type, size y URL/referencia si esta disponible.
4. Recuperar issue links y subtasks con key, summary y status.
5. Preservar el texto exacto de campos relevantes; no normalizar antes de validar.
6. Entregar un snapshot estructurado y marcar campos no disponibles como UNKNOWN.

Usar `references/reader-contract.md` para el shape esperado.
