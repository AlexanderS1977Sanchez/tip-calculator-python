def print_header() -> None:
    print("=" * 45)
    print("TIP CALCULATOR (Python CLI Project)")
    print("=" * 45)


def print_summary(
    bill_amount: float,
    tip_percent: float,
    tip: float,
    total: float,
    people: int,
    per_person: float,
) -> None:
    print("\n--- Summary ---")
    print(f"Bill amount:      ${bill_amount:.2f}")
    print(f"Tip percentage:   {tip_percent:.2f}%")
    print(f"Tip amount:       ${tip:.2f}")
    print(f"Total amount:     ${total:.2f}")

    if people > 1:
        print(f"People:           {people}")
        print(f"Per person:       ${per_person:.2f}")
    print("-" * 30 + "\n")


def print_goodbye() -> None:
    print("Thanks for using the Tip Calculator. Goodbye!")