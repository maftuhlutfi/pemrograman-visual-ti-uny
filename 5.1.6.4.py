def readint(prompt, min, max):
    try:
        v = int(input(prompt))
        assert v >= min and v <= max
        return v
    except ValueError:
        print("Error: wrong input")
        return readint(prompt, min, max)
    except AssertionError:
        print("Error: the value is not within permitted range (min..max")
        return readint(prompt, min, max)

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)