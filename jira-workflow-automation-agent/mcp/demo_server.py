from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-demo")

@mcp.tool()
def get_agent_context(topic: str) -> dict:
    """Return demo-only contextual guidance. Replace with an authorized enterprise source in real deployments."""
    return {"topic": topic, "domain": 'Jira/workflow', "source": "demo-local", "warning": "No enterprise data is exposed by this demo MCP server."}

@mcp.tool()
def validate_change(summary: str) -> dict:
    """Run a deterministic demo validation checklist over a change summary."""
    missing=[]
    text=summary.lower()
    for key in ["test","rollback","risk"]:
        if key not in text: missing.append(key)
    return {"ok": not missing, "missing_signals": missing, "summary": summary}

if __name__ == "__main__":
    mcp.run(transport="stdio")
