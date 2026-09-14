# GitHub Copilot custom agents and parallel orchestration

Official references used for this workspace:
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents

Design note: GitHub Copilot custom agents can be executed as subagents with isolated context. When independent tasks can be split, the runtime supports parallel subagent orchestration/Fleet patterns. The local Python demo is deterministic and demonstrates the same fan-out/fan-in control flow without requiring a live Copilot runtime.
