from cli_io import ask_text, ask_number, ask_whole_number, show_message, show_transaction


def main() -> None:
    show_message("=== Personal Finance Tracker ===")
    name: str = ask_text("What is your name? ")
    description: str = ask_text("What did you buy? ")
    unit_price: float = ask_number("Price of one item: ")
    quantity: int = ask_whole_number("How many items? ")
    total: float = unit_price * quantity
    show_message(f"Thanks, {name}. Here is your record:")
    show_transaction(description, total)


if __name__ == "__main__":
    main()