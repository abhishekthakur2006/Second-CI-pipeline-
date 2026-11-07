def is_pangram(text: str) -> bool:
    """Return whether text contains every letter of the English alphabet."""
    return set("abcdefghijklmnopqrstuvwxyz").issubset(text.lower())
