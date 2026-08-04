def get_count_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_count_characters(text: str) -> dict[str, int]:
    charater_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in charater_dict:
            charater_dict[char_lower] = 1
        else:
            charater_dict[char_lower] += 1
    return charater_dict

def sort_on(character_count:tuple[str, int]) -> int:
     return character_count[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []
    for char in char_dict:
        count = char_dict[char]
        sorted_list.append((char, count))

    sorted_list = sorted(sorted_list, key=sort_on, reverse=True)

    return sorted_list
