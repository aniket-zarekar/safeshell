#!/usr/bin/env python3
"""Starter safety checker agent for SafeShell."""

import os
import sys

from safeshell.evaluator import evaluate_command


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 agent.py '<command>'")
        return 1

    command = " ".join(sys.argv[1:])
    cwd = os.getcwd()
    assessment = evaluate_command(command, cwd)

    print(f"Risk level: {assessment.risk_level}")
    print(f"Destructive: {assessment.is_destructive}")
    print(f"Summary: {assessment.summary}")
    print(f"Blast radius: {assessment.blast_radius}")
    if assessment.safe_alternative:
        print(f"Safer alternative: {assessment.safe_alternative}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
