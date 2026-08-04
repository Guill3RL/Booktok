def get_count_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_count_characters(text: str) -> dict[str: int]:
    charater_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in charater_dict:
            charater_dict[char_lower] = 1
        else:
            charater_dict[char_lower] += 1
    return charater_dict
