def concatenate(s1: str, s2: str) -> str:
    long_word = s1 + s2
    if len(long_word) > 10:
        return "Too long!"
    else:
        return long_word




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
