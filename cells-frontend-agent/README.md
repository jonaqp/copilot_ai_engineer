# Cells / Frontend Agent

Asistente de desarrollo frontend orientado a componentes Cells, accesibilidad, calidad, pruebas y experiencia de usuario.

## Qué incluye

- Aplicación demo Flask (`app.py`) con UI y endpoint `POST /api/agent-plan`.
- Perfil GitHub Copilot en `.github/agents/cells-frontend-agent.agent.md`.
- Skills reutilizables en `.github/skills/`.
- Configuración oficial de GitHub MCP Server para VS Code en `.vscode/mcp.json`.
- MCP local de demostración sin datos corporativos en `.github/mcp/demo_server.py`.
- Guías de modelo, MCP, seguridad y uso.
- Tests de humo con pytest.

## Inicio rápido

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
python app.py
```

Abrir `http://127.0.0.1:5000`.

## Uso con GitHub Copilot

1. Abrir esta carpeta como workspace en VS Code con GitHub Copilot habilitado.
2. Verificar que el perfil aparezca en el selector de agentes.
3. Iniciar GitHub MCP Server desde la configuración del workspace. La opción incluida usa OAuth mediante Docker y callback local.
4. Seleccionar **Cells / Frontend Agent** y pedir una tarea concreta.
5. Copilot cargará las Skills cuando su descripción coincida con la tarea.

## Importante

Los detalles APX/Cells/Jira/producción específicos de una organización deben conectarse mediante documentación o MCP autorizados. Este paquete no inventa endpoints, políticas ni convenciones propietarias. Sustituir el MCP demo por fuentes corporativas aprobadas antes de uso real.
