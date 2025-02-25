import sys

from stats import count_words_in_text, character_count, sort_character_frequencies


def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words_in_text(book_text)
    char_frequency = character_count(book_text)
    sorted_char_list = sort_character_frequencies(char_frequency)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_list:
        char, count = list(char_dict.items())[0]
        print(f"{char}: {count}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    print(sys.argv)
    sys.exit(1)
else:
    main()