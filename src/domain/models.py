"""Domain models module."""

from dataclasses import dataclass
from typing import Any


@dataclass
class Data:
    """Data domain model."""

    id: str
    content: str
    metadata: dict[str, Any] | None
