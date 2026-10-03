"""Print the Collatz sequence for 27 and its transition count."""


def collatz_sequence(start: int) -> list[int]:
    """Return the sequence from start through the terminal value 1."""
    sequence = [start]
    while sequence[-1] != 1:
        current = sequence[-1]
        sequence.append(current // 2 if current % 2 == 0 else 3 * current + 1)
    return sequence


def main() -> None:
    sequence = collatz_sequence(27)
    for number in sequence:
        print(number)
    print(f"Transitions/steps to reach 1: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
