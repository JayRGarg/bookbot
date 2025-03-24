from typing import Dict

def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_counts(text: str) -> Dict[str, int]:
    text = text.lower()
    res = {word : text.count(word) for word in set(text)}
    return res
