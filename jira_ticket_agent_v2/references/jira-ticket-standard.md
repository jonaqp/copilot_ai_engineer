# Jira Ticket Standard - perfil deployment-datax

Este perfil se deriva de las tres referencias visuales incluidas en `docs/screenshots/` y esta pensado para una demo de pase a produccion DataX/PFCO. No asumir que aplica a todos los proyectos Jira.

## 1. Resumen / Summary
Formato de referencia:
`[Peru - <EQUIPO>] DataX - <PLATAFORMA> - <ID> - Pase a produccion`

Validar:
- prefijo de pais/equipo entre corchetes;
- dominio/tecnologia (ej. DataX);
- plataforma o iniciativa;
- identificador funcional/tecnico;
- finalidad `Pase a produccion` cuando aplique.

## 2. Campos de readiness
Verificar si estan disponibles en Jira:
- Priority
- Team Backlog
- Geography / Workspace Geography
- Feature Link
- Item Type
- Tech Stack
- Definition of Ready completa
- Definition of Done completa
- Acceptance Criteria completa
- Story Points
- Sprint / Sprint Estimate
- Impediment
- Status / Resolution / Due date

No asumir PASS si un campo no fue recuperado.

## 3. Descripcion
La referencia visual contiene una seccion `Informacion General` con:
- tabla Componente / Cantidad;
- Proyecto Finalista;
- UUAA;
- Namespace;
- Folder/Malla Control-M;
- Periodicidad;
- Hora;
- Origen;
- Destino;
- MSA;
- Adaptadores y atributos tecnicos;
- Bloques;
- Transfers;
- DataObjects;
- Schemas ORIGEN/DESTINO.

Validar estructura, legibilidad, valores vacios/N/A justificados y consistencia de cantidades con los elementos listados.

## 4. Adjuntos
La referencia visual muestra ejemplos de:
- evidencia DQA (JPG/PNG);
- captura/evidencia de ejecucion;
- matriz de escalamiento (PNG/XLSX).

Validar existencia, nombre, extension, tamano no cero y relacion con el proposito del ticket. Si el contenido binario se puede descargar, validar que la imagen se abra y sea legible. Si no se puede descargar, marcar inspeccion visual como UNKNOWN_VISUAL.

## 5. Issue links
Validar que las relaciones esperadas existan y tengan semantica coherente, por ejemplo:
- `in Deployment`
- `is child item of`
- `tested by`

Validar tambien estado del ticket relacionado si la API lo expone.

## 6. Subtasks
Validar que:
- existan las subtareas requeridas por el perfil/proyecto;
- cada subtask tenga key, resumen, estado y assignee cuando corresponda;
- las subtareas bloqueantes no esten pendientes antes de declarar READY.

## 7. Decision
- READY: todas las reglas obligatorias PASS y sin UNKNOWN criticos.
- READY WITH CONDITIONS: no hay FAIL bloqueantes pero existen WARNING/UNKNOWN no criticos.
- NOT READY: uno o mas FAIL bloqueantes o UNKNOWN criticos.
