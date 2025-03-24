from stats import get_num_words, get_char_counts

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    txt = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(txt)
    char_count = get_char_counts(txt)
    print(f"{word_count} words found in the document")
    print(char_count)

main()
