from src.validations import ensure_positive, ensure_non_negative, ensure_int_at_least


def get_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            ensure_positive(value, "Bill amount")
            return value
        except ValueError:
            print("Invalid input. Please enter a number greater than 0 (example: 25.50).")


def get_non_negative_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            ensure_non_negative(value, "Tip percentage")
            return value
        except ValueError:
            print("Invalid input. Please enter a number 0 or greater (example: 12).")


def get_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            ensure_int_at_least(value, 1, "Number of people")
            return value
        except ValueError:
            print("Invalid input. Please enter an integer 1 or greater (example: 3).")


def get_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please answer with 'y'/'yes' or 'n'/'no'.")