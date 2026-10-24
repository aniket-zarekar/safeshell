#!/usr/bin/env python3
import sys
import os
import subprocess
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

SYSTEM_PROMPT = """
You are an operating system safety firewall for terminal shell commands.
Analyze the target command given the working context.
Evaluate:
1. Is it destructive (deleting data, wiping volumes, killing processes)?
2. Does it touch outside the current working directory?
3. What is the blast radius?

Respond ONLY with valid JSON in this exact structure:
{
  "risk_level": "LOW" | "MEDIUM" | "HIGH" | "CRITICAL",
  "is_destructive": true | false,
  "summary": "1 sentence describing what this command actually does",
  "blast_radius": "Concise bullet point of consequences",
  "safe_alternative": "Optional safer command or null"
}
"""

def analyze_command(command: str, cwd: str) -> dict:
    prompt = f"Target Command: {command}\nCurrent Working Directory: {cwd}\nUser: {os.getenv('USER', 'developer')}"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {
            "risk_level": "MEDIUM",
            "is_destructive": True,
            "summary": "Could not contact LLM safety evaluator.",
            "blast_radius": f"Error: {str(e)}",
            "safe_alternative": None
        }

def main():
    if len(sys.argv) < 2:
        print(f"{YELLOW}Usage:{RESET} guard <command to run>")
        sys.exit(1)

    command_str = " ".join(sys.argv[1:])
    cwd = os.getcwd()

    print(f"\n{CYAN}🔍 Inspecting:{RESET} {BOLD}{command_str}{RESET}")
    eval_result = analyze_command(command_str, cwd)

    risk = eval_result.get("risk_level", "LOW")
    is_destructive = eval_result.get("is_destructive", False)
    summary = eval_result.get("summary", "")
    blast = eval_result.get("blast_radius", "")
    alt = eval_result.get("safe_alternative")

    if risk == "LOW" and not is_destructive:
        print(f"{GREEN}✓ Safe to execute.{RESET}\n")
        subprocess.run(command_str, shell=True)
        return

    color = RED if risk in ["HIGH", "CRITICAL"] else YELLOW
    print(f"\n{color}{BOLD}⚠️  FIREWALL WARNING [{risk} RISK]{RESET}")
    print(f"• {BOLD}Action:{RESET} {summary}")
    print(f"• {BOLD}Blast Radius:{RESET} {color}{blast}{RESET}")
    if alt:
        print(f"• {BOLD}Safer Alternative:{RESET} {CYAN}{alt}{RESET}")

    try:
        confirm = input(f"\n{BOLD}Do you want to proceed? [y/N]: {RESET}").strip().lower()
        if confirm == 'y':
            print(f"{GREEN}Executing...{RESET}\n")
            subprocess.run(command_str, shell=True)
        else:
            print(f"{RED}Aborted.{RESET} Command was cancelled.")
            sys.exit(0)
    except KeyboardInterrupt:
        print(f"\n{RED}Aborted.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
