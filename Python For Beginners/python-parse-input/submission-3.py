from typing import List

def read_integers() -> List[int]:
    integers = input().split(",")
    integer_list = []

    for i in integers:
        integer_list.append(int(i))
    return integer_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
