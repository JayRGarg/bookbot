from typing import Dict, List

def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_counts(text: str) -> Dict[str, int]:
    text = text.lower()
    res = {word : text.count(word) for word in set(text)}
    #del res[" "]
    return res

def get_sorted_dicts(char_counts: Dict[str, int]) -> List[Dict[str, int]]:
    lst = [{"char": k, "count": v} for k, v in char_counts.items()]
    lst.sort(key=lambda x: x["count"], reverse=True)
    return lst
