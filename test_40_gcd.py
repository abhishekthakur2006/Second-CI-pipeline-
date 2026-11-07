import importlib


module = importlib.import_module("40_gcd")


def test_finds_gcd() -> None:
    assert module.gcd(48, 18) == 6


def test_gcd_handles_zero_and_negative_inputs() -> None:
    assert module.gcd(0, 9) == 9
    assert module.gcd(-12, 8) == 4
    assert module.gcd(0, 0) == 0
