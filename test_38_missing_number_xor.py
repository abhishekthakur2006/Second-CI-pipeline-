import importlib


module = importlib.import_module("38_missing_number_xor")


def test_finds_missing_number() -> None:
    assert module.find_missing_number([3, 0, 1]) == 2


def test_finds_missing_first_or_last_number() -> None:
    assert module.find_missing_number([1, 2, 3]) == 0
    assert module.find_missing_number([0, 1, 2]) == 3


def test_empty_sequence_is_missing_zero() -> None:
    assert module.find_missing_number([]) == 0
