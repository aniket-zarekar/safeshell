import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandAssessment:
    risk_level: str
    is_destructive: bool
    summary: str
    blast_radius: str
    safe_alternative: Optional[str] = None
