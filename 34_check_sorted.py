from collections.abc import Sequence
from typing import Any


def is_sorted(values: Sequence[Any]) -> bool:
    """Return whether values are in non-decreasing order."""
    return all(values[index] <= values[index + 1] for index in range(len(values) - 1))
