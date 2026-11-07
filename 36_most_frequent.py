from collections import Counter
from collections.abc import Sequence
from typing import Any, Optional


def most_frequent(values: Sequence[Any]) -> Optional[Any]:
    """Return the most frequent value; ties go to the first occurrence."""
    if not values:
        return None

    counts = Counter(values)
    highest_count = max(counts.values())
    return next(value for value in values if counts[value] == highest_count)
