# QA & Testing Agent

Aplicación de demo independiente para PyCharm + GitHub Copilot.

## Modelo

**Claude Sonnet 5**. Solo se recomiendan modelos Claude/Anthropic. Alternativa: Claude Haiku 4.5 / Claude Opus 5.

## Skills

- `coverage-review`
- `qa-pr-readiness`
- `qa-ticket-jira`
- `unit-test`
- `xray-generator`

## MCP

- GitHub Enterprise BBVA remoto: `mcp/remote/github-bbva.jetbrains.json`.
- GitHub local Docker: `mcp/local/github-docker.jetbrains.json`.
- Dominio local `qa-local`: `mcp/local/domain-local.jetbrains.json`.
- Catálogo Cells/Figma/GitHub: `mcp/remote/catalog-all-observed.jetbrains.json` y `mcp/local/catalog-all-observed-local.jetbrains.json`.

Ver `docs/MCP_GUIDE.md` y `prompts/CASOS_DE_USO.md`.

## Demo sin servicios externos

```bash
python scripts/run_demo_flow.py
python scripts/test_local_mcp.py
```

## Flask

```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```
