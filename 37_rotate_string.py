def rotate_string(text: str, positions: int) -> str:
    """Rotate text right by positions; negative values rotate left."""
    if not text:
        return text

    offset = positions % len(text)
    if offset == 0:
        return text
    return text[-offset:] + text[:-offset]
