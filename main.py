def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"Found {num_words} total words")


main()
