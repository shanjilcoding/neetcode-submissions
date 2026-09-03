def add_two_numbers() -> int:
    integer = input().split(",")
    sumint = 0
    for i in integer:
        sumint += int(i)
    return sumint



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
