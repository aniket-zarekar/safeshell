#!/usr/bin/env python3
import os
import subprocess
import sys

from safeshell.evaluator import evaluate_command

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def main() -> int:
    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage:{RESET} guard <command to run>")
        return 1

    command_str = " ".join(sys.argv[1:])
    cwd = os.getcwd()
    assessment = evaluate_command(command_str, cwd)

    print(f"\n{CYAN}🔍 Inspecting:{RESET} {BOLD}{command_str}{RESET}")

    risk = assessment.risk_level
    is_destructive = assessment.is_destructive

    if risk == "LOW" and not is_destructive:
        print(f"{GREEN}✓ Safe to execute.{RESET}\n")
        subprocess.run(command_str, shell=True)
        return 0

    color = RED if risk in {"HIGH", "CRITICAL"} else YELLOW
    print(f"\n{color}{BOLD}⚠️  FIREWALL WARNING [{risk} RISK]{RESET}")
    print(f"• {BOLD}Action:{RESET} {assessment.summary}")
    print(f"• {BOLD}Blast Radius:{RESET} {color}{assessment.blast_radius}{RESET}")
    if assessment.safe_alternative:
        print(f"• {BOLD}Safer Alternative:{RESET} {CYAN}{assessment.safe_alternative}{RESET}")

    try:
        confirm = input(f"\n{BOLD}Do you want to proceed? [y/N]: {RESET}").strip().lower()
        if confirm in {"y", "yes"}:
            print(f"{GREEN}Executing...{RESET}\n")
            subprocess.run(command_str, shell=True)
            return 0
        print(f"{RED}Aborted.{RESET} Command was cancelled.")
        return 0
    except KeyboardInterrupt:
        print(f"\n{RED}Aborted.{RESET}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
