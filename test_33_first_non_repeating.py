import importlib


module = importlib.import_module("33_first_non_repeating")


def test_finds_first_non_repeating_character() -> None:
    assert module.first_non_repeating_character("swiss") == "w"


def test_returns_none_when_every_character_repeats() -> None:
    assert module.first_non_repeating_character("aabb") is None


def test_empty_string_returns_none() -> None:
    assert module.first_non_repeating_character("") is None
