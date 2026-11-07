from collections.abc import Sequence


def find_missing_number(values: Sequence[int]) -> int:
    """Find the missing value from the integers 0 through len(values)."""
    missing = len(values)
    for index, value in enumerate(values):
        missing ^= index ^ value
    return missing
