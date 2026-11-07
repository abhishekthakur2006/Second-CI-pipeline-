import importlib

import pytest


module = importlib.import_module("39_transpose_matrix")


def test_transposes_matrix() -> None:
    assert module.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


def test_transposes_empty_matrix() -> None:
    assert module.transpose_matrix([]) == []


def test_rejects_ragged_matrix() -> None:
    with pytest.raises(ValueError, match="rectangular"):
        module.transpose_matrix([[1, 2], [3]])
