from src.inputs import get_positive_float, get_non_negative_float, get_positive_int, get_yes_no
from src.calculator import calculate_tip, calculate_total, calculate_per_person
from src.display import print_header, print_summary, print_goodbye


def run_tip_calculator() -> None:
    print_header()

    while True:
        bill_amount = get_positive_float("Enter the bill amount (e.g., 25.50): ")
        tip_percent = get_non_negative_float("Enter the tip percentage (e.g., 10, 12, 15): ")

        split = get_yes_no("Do you want to split the bill? (y/n): ")
        people = 1
        if split:
            people = get_positive_int("How many people? (min 1): ")

        tip = calculate_tip(bill_amount, tip_percent)
        total = calculate_total(bill_amount, tip)
        per_person = calculate_per_person(total, people)

        print_summary(
            bill_amount=bill_amount,
            tip_percent=tip_percent,
            tip=tip,
            total=total,
            people=people,
            per_person=per_person,
        )

        again = get_yes_no("Calculate another tip? (y/n): ")
        if not again:
            break

    print_goodbye()


if __name__ == "__main__":
    run_tip_calculator()