﻿blocks = int(input("Enter the number of blocks: "))

height = 0;

while height < blocks:
    height += 1
    blocks -= height

print("The height of the pyramid:", height)