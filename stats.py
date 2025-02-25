def count_words_in_text(text):
    words = text.split()
    return len(words)


def character_count(text):

    char_frequency = {}

    text = text.lower()

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    return char_frequency


def sort_character_frequencies(char_frequency):
    sorted_char_list = sorted(
        [{char: count} for char, count in char_frequency.items() if char.isalpha()],
        key=lambda x: list(x.values())[0],
        reverse=True
    )
    return sorted_char_list