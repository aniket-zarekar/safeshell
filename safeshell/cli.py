#!/usr/bin/env python3
"""Command-line entry for SafeShell."""

from safeshell.evaluator import evaluate_command


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Safely review shell commands before execution.")
    parser.add_argument("command", nargs="+", help="The shell command to assess")
    args = parser.parse_args()

    command = " ".join(args.command)
    assessment = evaluate_command(command, cwd=".")

    print(f"Risk level: {assessment.risk_level}")
    print(f"Destructive: {assessment.is_destructive}")
    print(f"Summary: {assessment.summary}")
    print(f"Blast radius: {assessment.blast_radius}")
    if assessment.safe_alternative:
        print(f"Safer alternative: {assessment.safe_alternative}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
