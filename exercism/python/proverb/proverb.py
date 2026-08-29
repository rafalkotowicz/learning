"""Generate the traditional 'For want of a nail' proverb."""


def proverb(*pieces: str, qualifier: str | None = None) -> list[str]:
    """Build proverb lines from an arbitrary number of input pieces.

    Args:
        *pieces: Ordered proverb elements, e.g. "nail", "shoe", "horse".
        qualifier: Optional word inserted before the first piece in final line.

    Returns:
        A list of proverb lines.
    """
    if not pieces:
        return []

    lines = [
        f"For want of a {lost_item} the {consequence} was lost."
        for lost_item, consequence in zip(pieces, pieces[1:])
    ]
    first_piece = pieces[0]
    if qualifier:
        lines.append(f"And all for the want of a {qualifier} {first_piece}.")
    else:
        lines.append(f"And all for the want of a {first_piece}.")
    return lines
