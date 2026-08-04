from stats import get_count_words, get_count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(file_path: str, num_words: int, num_characters: list[tuple[str, int]]):
    header =             "============ BOOKBOT ============"
    route =             f"Analyzing book found at {file_path}..."
    section_word_count = "----------- Word Count ----------"
    word_count_txt =    f"Found {num_words} total words"
    section_char_count = "--------- Character Count -------"
    footer =             "============= END ==============="

    print(header)
    print(route)
    print(section_word_count)
    print(word_count_txt)
    print(section_char_count)

    for char in num_characters:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")

    print(footer)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_count_words(book)
    num_characters = get_count_characters(book)
    num_characters = chars_dict_to_sorted_list(num_characters)
    print_report(book_path, num_words, num_characters)


main()
