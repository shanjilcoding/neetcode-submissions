def remove_fourth_character(word: str) -> str:
    first_word = word[:3]
    second_word = word[4:]
    final = first_word + second_word
    return final


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
