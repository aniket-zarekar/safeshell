# Agents

This directory contains agent-oriented projects and task-focused workflow components for SafeShell.

## Current contents

- `safety-checker/` — a starter agent that evaluates the safety of shell commands before execution.

## Agent standards

Each agent should:

- provide a clear purpose
- document setup and usage
- keep decisions explainable
- respect safety constraints

## Example

```bash
python3 agents/safety-checker/agent.py "rm -rf /tmp/demo"
```
