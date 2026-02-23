from src.validations import ensure_positive, ensure_non_negative, ensure_int_at_least


def calculate_tip(bill_amount: float, tip_percent: float) -> float:
    """
    Tip = bill_amount * (tip_percent / 100)
    """
    ensure_positive(bill_amount, "Bill amount")
    ensure_non_negative(tip_percent, "Tip percentage")
    return bill_amount * (tip_percent / 100.0)


def calculate_total(bill_amount: float, tip: float) -> float:
    """
    Total = bill_amount + tip
    """
    ensure_positive(bill_amount, "Bill amount")
    ensure_non_negative(tip, "Tip")
    return bill_amount + tip


def calculate_per_person(total: float, people: int) -> float:
    """
    Per person = total / people
    """
    ensure_positive(total, "Total")
    ensure_int_at_least(people, 1, "Number of people")
    return total / people