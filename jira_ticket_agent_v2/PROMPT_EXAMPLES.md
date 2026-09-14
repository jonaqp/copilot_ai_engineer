# Prompts

## Solo analizar
Analiza el ticket DEDATIOCL1-20846 con `jira-ticket-quality` usando `mcp-atlassian`. No modifiques Jira. Revisa formato1/formato2/formato3: summary, informacion general, DoR/DoD, Acceptance Criteria, adjuntos, relaciones y subtareas. Devuelve tabla de evidencias y decision final.

## Proponer correcciones
Revisa DEDATIOCL1-21347 y prepara un patch de summary/description si el formato no cumple. No escribas aun. Muestra antes/despues y explica cada cambio.

## Corregir y revalidar
Aplica el patch aprobado a DEDATIOCL1-21347 usando mcp-atlassian. No borres adjuntos, links ni subtareas. Relee el ticket y ejecuta nuevamente el quality gate.

## Revisar imagenes
Valida los adjuntos del ticket. Si puedes descargar las imagenes, comprueba que abran y sean legibles. Si solo puedes ver metadata, marca UNKNOWN_VISUAL y no inventes el contenido.
