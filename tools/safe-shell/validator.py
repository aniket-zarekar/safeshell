from safeshell.evaluator import evaluate_command


def validate_command(command: str, cwd: str = "."):
    return evaluate_command(command, cwd)
