"""SafeShell package."""

from .evaluator import evaluate_command
from .models import CommandAssessment

__all__ = ["CommandAssessment", "evaluate_command"]
