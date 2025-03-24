import sys
from stats import get_num_words, get_char_counts, get_sorted_dicts

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

    txt = get_book_text(path)
    word_count = get_num_words(txt)
    char_count = get_char_counts(txt)
    lst_chars = get_sorted_dicts(char_count)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in lst_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()
