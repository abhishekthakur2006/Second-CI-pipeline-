import importlib


module = importlib.import_module("36_most_frequent")


def test_finds_most_frequent_element() -> None:
    assert module.most_frequent([1, 3, 1, 2, 1, 3]) == 1


def test_tie_uses_first_occurring_value() -> None:
    assert module.most_frequent(["b", "a", "a", "b"]) == "b"


def test_empty_list_returns_none() -> None:
    assert module.most_frequent([]) is None
