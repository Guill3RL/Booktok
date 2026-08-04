from stats import get_count_words, get_count_characters

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_count_words(book)
    num_characters = get_count_characters(book)
    print(f"Found {num_words} total words")
    print(num_characters)


main()
