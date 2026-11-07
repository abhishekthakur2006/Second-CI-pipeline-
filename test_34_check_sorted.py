import importlib


module = importlib.import_module("34_check_sorted")


def test_sorted_values() -> None:
    assert module.is_sorted([1, 2, 2, 5]) is True


def test_unsorted_values() -> None:
    assert module.is_sorted([1, 3, 2]) is False


def test_empty_and_single_item_lists_are_sorted() -> None:
    assert module.is_sorted([]) is True
    assert module.is_sorted([7]) is True
