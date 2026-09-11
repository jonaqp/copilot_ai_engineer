from flask import Flask, jsonify, render_template, request
from agent_config import AGENT

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html", agent=AGENT)

@app.get("/health")
def health():
    return jsonify({"status":"ok","agent":AGENT["name"]})

@app.get("/api/config")
def config():
    return jsonify(AGENT)

@app.post("/api/agent-plan")
def agent_plan():
    data=request.get_json(silent=True) or {}
    task=(data.get("task") or "").strip()
    if not task:
        return jsonify({"error":"task is required"}),400
    return jsonify({
      "agent":AGENT["name"],
      "task":task,
      "recommended_model":AGENT["recommended_model"],
      "skills":AGENT["skills"],
      "mcp":AGENT["mcp"],
      "copilot_prompt":f"Use the {AGENT['name']} custom agent. Task: {task}. Inspect repository evidence before editing, apply the relevant skills, use MCP only with least privilege, validate results, and summarize evidence, changes, tests and residual risks."
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
