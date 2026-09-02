from typing import List

def contains_duplicate(words: List[str]) -> bool:
    initial_len = len(words)

    test_set = set(words)
    after_len = len(test_set)

    if initial_len > after_len:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
