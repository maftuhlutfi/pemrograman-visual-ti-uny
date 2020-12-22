steps = 0
c0 = int(input("Enter the number: "))

while c0 != 1:
    steps += 1
    if c0 % 2:
        c0 = 3 * c0 + 1
        print(c0)
    else:
        c0 //= 2
        print(c0)
        
print("steps = ", steps)