import re


def count_word_frequencies(text: str) -> dict[str, int]:
    """Return case-insensitive word counts from text."""
    frequencies: dict[str, int] = {}
    words = re.findall(r"[\w']+", text.casefold())
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def main() -> None:
    """Read text and display each word's frequency."""
    text = input("Enter a sentence or paragraph: ").strip()
    frequencies = count_word_frequencies(text)

    if not frequencies:
        print("No words were found.")
        return

    print("\n========== WORD FREQUENCIES ==========")
    print(f"{'Word':<25} Count")
    print("-" * 33)
    for word, count in sorted(frequencies.items()):
        print(f"{word:<25} {count}")


if __name__ == "__main__":
    main()
