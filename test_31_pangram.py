import importlib


module = importlib.import_module("31_pangram")


def test_pangram_true() -> None:
    assert module.is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_pangram_false() -> None:
    assert module.is_pangram("Hello World") is False
