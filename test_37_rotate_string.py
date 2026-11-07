import importlib


module = importlib.import_module("37_rotate_string")


def test_rotates_string_right() -> None:
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_wraps_positions_and_handles_negative_values() -> None:
    assert module.rotate_string("abc", 4) == "cab"
    assert module.rotate_string("abc", -1) == "bca"


def test_empty_string_remains_empty() -> None:
    assert module.rotate_string("", 3) == ""
