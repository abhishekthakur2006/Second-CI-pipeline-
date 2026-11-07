from typing import Optional


def first_non_repeating_character(text: str) -> Optional[str]:
    """Return the first character occurring once, or None if there is none."""
    counts = {character: text.count(character) for character in set(text)}
    return next((character for character in text if counts[character] == 1), None)
