def ensure_positive(value: float, field_name: str) -> None:
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than 0.")


def ensure_non_negative(value: float, field_name: str) -> None:
    if value < 0:
        raise ValueError(f"{field_name} must be 0 or greater.")


def ensure_int_at_least(value: int, minimum: int, field_name: str) -> None:
    if value < minimum:
        raise ValueError(f"{field_name} must be at least {minimum}.")