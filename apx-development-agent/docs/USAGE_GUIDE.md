# Guía de uso - APX Development Agent

## 1. Preparar entorno

Instalar Python 3.11+, Docker Desktop, VS Code y GitHub Copilot. Crear el virtualenv, instalar `requirements.txt` y ejecutar `pytest -q`.

## 2. Levantar demo Flask

Ejecutar `python app.py` y abrir `http://127.0.0.1:5000`. La UI convierte una petición en un plan: agente, Skills, MCP y prompt listo para Copilot.

## 3. Activar GitHub MCP

Abrir el workspace en VS Code. Aceptar/arrancar el servidor MCP configurado en `.vscode/mcp.json`. La primera ejecución con OAuth puede solicitar autenticación en navegador.

## 4. Usar el agente

Seleccionar `APX Development Agent` en Copilot Agent mode. Ejemplos:

- `Analiza este componente APX antes de modificarlo y prepara un plan de cambio.`
- `Revisa este diff APX e identifica riesgos, dependencias y pruebas necesarias.`
- `Genera una estrategia de pruebas para un cambio online/batch.`

## 5. Validar antes de aceptar cambios

Revisar diff, ejecutar tests/build/lint reales, comprobar que no hay secretos y confirmar las acciones externas. Para producción, conservar revisión humana en decisiones de go/no-go y en escrituras sobre sistemas externos.

## 6. Conectar contexto corporativo

Añadir un MCP autorizado o referencias internas. No copiar documentación sensible dentro de la Skill si debe permanecer en un sistema controlado; preferir recuperación bajo demanda con permisos.
