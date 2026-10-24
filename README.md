# SafeShell

SafeShell is a security-focused shell command safety layer designed to help users evaluate and control risky terminal actions before execution.

## Overview

This repository contains a small but practical safety framework for command-line tools. The core idea is simple: before executing a shell command, inspect its intent, estimate the blast radius, and block or confirm risky actions when needed.

## Why this project exists

Modern developer workflows often involve commands that can accidentally delete files, modify system paths, affect other users, or wipe critical data. SafeShell provides a lightweight review layer that helps users understand the consequences before a command is executed.

## Security model

SafeShell combines:

- rule-based security checks for common destructive patterns
- optional LLM-backed evaluation through OpenAI when configured
- confirmation prompts for medium/high risk operations
- safer command suggestions when available

This makes the project useful both in local developer environments and as a foundation for more advanced shell safety tooling.

## Repository structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── guard.py
├── safeshell/
│   ├── __init__.py
│   ├── cli.py
│   ├── evaluator.py
│   ├── models.py
│   └── rules.py
├── agents/
│   ├── README.md
│   └── safety-checker/
│       ├── README.md
│       └── agent.py
├── tools/
│   ├── README.md
│   └── safe-shell/
│       ├── README.md
│       ├── __init__.py
│       ├── cli.py
│       └── validator.py
├── template/
│   ├── README.md
│   ├── .gitignore
│   └── .env.example
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
└── .github/workflows/
    └── ci.yml
```

## Quick start

1. Clone the repository.
2. Install dependencies.
3. Export your API key if you want OpenAI-based evaluation.
4. Run the guard command.

```bash
git clone https://github.com/aniket-zarekar/safeshell.git
cd safeshell
python3 -m pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
python3 guard.py "ls"
```

## Example usage

```bash
python3 guard.py "ls -la"
python3 guard.py "rm -rf /tmp/demo"
python3 guard.py "find . -name '*.py' -delete"
```

## Risk levels

- LOW: safe or routine command
- MEDIUM: may affect local files or project state
- HIGH: likely destructive or modifies system state
- CRITICAL: severe or unsafe system-wide risk

## Safety philosophy

- Safe commands should run without interruption.
- Risky commands should be reviewed before execution.
- Destructive commands should include explicit confirmation.
- Users should see the reason and the likely blast radius.

## Roadmap

- expand rule-based checks for system-level commands
- add a richer agent interface for policy enforcement
- support team-safe command templates and allowlists
- integrate CI checks and automated validation

## License

This project is intended as a starter framework and may be extended for your own workflow or internal tooling requirements.
