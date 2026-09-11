# MCP - guía para Security & Hardening Agent

## Servidores disponibles

1. `bbva-github` remoto sobre `https://copilot-api.bbva.ghe.com/mcp`, con toolsets mínimos para el agente.
2. `bbva-github-local` con la imagen oficial `ghcr.io/github/github-mcp-server`; definir `GITHUB_HOST` y credencial mediante el mecanismo aprobado.
3. `security-local` local Python/stdio para la demo.
4. Cells Docs, Figma remoto y Figma Desktop aparecen en el catálogo distribuido, pero no se habilitan en este agente salvo necesidad real.

## Regla

No usar `all` automáticamente. Reducir herramientas, mantener lectura por defecto y solicitar confirmación antes de escrituras.
