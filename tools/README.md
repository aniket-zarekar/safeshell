# Tools

This directory contains reusable tooling and operational utilities for the SafeShell ecosystem.

## Current contents

- `safe-shell/` — a CLI helper package for evaluating commands and validating safety rules.

## Tool expectations

Each tool should document:

- purpose
- usage
- required environment variables
- expected output

## Example

```bash
python3 tools/safe-shell/cli.py "ls -la"
```
