#!/usr/bin/env python3
"""Tooling CLI for SafeShell validation."""

import sys

from safeshell.evaluator import evaluate_command


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py '<command>'")
        return 1

    command = " ".join(sys.argv[1:])
    assessment = evaluate_command(command, ".")
    print(assessment)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
