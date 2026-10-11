def ask_text(question: str) -> str:
    answer: str = input(question)
    return answer.strip()


def ask_number(question: str) -> float:
    answer: str = input(question)
    return float(answer)


def ask_whole_number(question: str) -> int:
    answer: str = input(question)
    return int(answer)


def show_message(message: str) -> None:
    print(message)


def show_transaction(description: str, amount: float) -> None:
    print(f"{description}: {amount:.2f}")