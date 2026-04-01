def clean(text: str) -> str:
    """
    Minimal cleaning:
    - Remove extra whitespace
    - Normalize newlines
    """
    return " ".join(text.split())

