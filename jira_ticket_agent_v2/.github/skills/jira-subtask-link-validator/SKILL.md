---
name: jira-subtask-link-validator
description: Revisa subtareas e issue links de un ticket Jira. Usar para validar relaciones como deployment, parent/child y tested-by, comprobar estados de tickets relacionados, subtareas obligatorias, responsables y blockers antes del cierre o pase a produccion.
---
# Workflow
1. Listar issue links con tipo, direccion, key y status del relacionado.
2. Listar subtasks con key, summary, status y assignee.
3. Comparar contra el perfil del ticket.
4. Marcar FAIL si falta una relacion/subtask declarada obligatoria o si una bloqueante no esta completada.
5. Marcar WARNING si la nomenclatura es ambigua pero la relacion existe.
6. No crear ni cerrar subtareas automaticamente.
