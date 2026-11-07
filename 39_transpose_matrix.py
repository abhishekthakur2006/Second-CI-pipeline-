from collections.abc import Sequence
from typing import Any


def transpose_matrix(matrix: Sequence[Sequence[Any]]) -> list[list[Any]]:
    """Return the transpose of a rectangular matrix."""
    if not matrix:
        return []

    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError("matrix must be rectangular")
    return [list(column) for column in zip(*matrix)]
