import importlib


module = importlib.import_module("35_move_zeros")


def test_moves_zeros_to_end_and_preserves_order() -> None:
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_handles_empty_and_all_zero_lists() -> None:
    assert module.move_zeros([]) == []
    assert module.move_zeros([0, 0]) == [0, 0]
