# Safety checker agent

This agent coordinates shell safety review using the core SafeShell evaluation logic.

## Purpose

The safety checker inspects a candidate shell command and returns a risk assessment.

## Usage

```bash
cd safeshell
python3 agents/safety-checker/agent.py "ls"
python3 agents/safety-checker/agent.py "rm -rf /tmp/demo"
```
