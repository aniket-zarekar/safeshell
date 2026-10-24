# Agents

This directory contains agent-oriented projects and task-focused system components.

## Purpose

Agents in this repository are expected to perform focused operational work such as:

- evaluating shell commands for risk
- enforcing safety constraints
- coordinating command execution flows
- supporting developer AI workflows

## Standards

Each agent directory should include:

- a clear purpose statement
- setup instructions
- input and output expectations
- safety or validation guidance

## Recommended structure

```text
agents/
├── README.md
└── <agent-name>/
    ├── README.md
    ├── main.py or entrypoint
    └── requirements.txt or config file
```

## Contribution pattern

When adding a new agent:

1. Create a dedicated directory in `agents/`.
2. Document the agent purpose and behavior.
3. Clearly describe its responsibilities and boundaries.
4. Ensure it does not bypass required safety checks.

## Notes

Agent implementations should favor explicit behavior, observability, and safe defaults over implicit automation.
