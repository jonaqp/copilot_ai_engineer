---
name: jira-ticket-writer
description: Aplica correcciones controladas a tickets Jira mediante mcp-atlassian despues de una validacion y autorizacion explicita. Usar para actualizar summary, description u otros campos permitidos, preservando informacion existente y revalidando el ticket despues de escribir.
---
# Workflow
1. Recibir key y patch aprobado.
2. Mostrar cambios `antes -> despues` si aun no fueron presentados.
3. Actualizar solo campos aprobados.
4. No borrar adjuntos, links, comentarios ni subtasks salvo orden explicita y confirmada.
5. Releer inmediatamente el issue.
6. Comparar valores escritos con valores recuperados.
7. Ejecutar nuevamente las skills de validacion relevantes.
8. Reportar campos aplicados, omitidos y cualquier error del MCP.
