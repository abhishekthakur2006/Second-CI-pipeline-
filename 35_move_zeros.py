from collections.abc import Sequence
from typing import Any


def move_zeros(values: Sequence[Any]) -> list[Any]:
    """Return a copy with all zeros moved to the end, preserving order."""
    non_zeros = [value for value in values if value != 0]
    return non_zeros + [value for value in values if value == 0]
