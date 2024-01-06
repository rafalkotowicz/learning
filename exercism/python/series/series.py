def verify_inputs(series: str, length: int) -> None:
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")


def slices(series: str, length: int) -> [str]:
    verify_inputs(series, length)
    return [series[i:i + length] for i in range(len(series) - length + 1)]
