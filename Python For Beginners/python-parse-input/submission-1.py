from typing import List

def read_integers() -> List[int]:
    integers = input()
    integer_list = []
    new_list = integers.split(",")

    for i in new_list:
        integer_list.append(int(i))
    return integer_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
