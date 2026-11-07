import importlib


module = importlib.import_module("32_count_words")


def test_count_words_in_sentence() -> None:
    assert module.count_words("Count the words in this sentence") == 6


def test_count_words_ignores_extra_whitespace() -> None:
    assert module.count_words("  one\t two\nthree  ") == 3


def test_count_words_empty_sentence() -> None:
    assert module.count_words("   ") == 0
