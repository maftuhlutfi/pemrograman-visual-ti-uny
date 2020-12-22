def digitOfLife(birth):
    digit = 0
    while len(birth) > 1:
        for c in birth:
            digit += int(c)
        birth = str(digit)
        digit = 0
    return birth

birth = input('Enter birth: ')
print(digitOfLife(birth))