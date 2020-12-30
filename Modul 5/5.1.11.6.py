def encrypt(text, shift):
    cipher = ''
    for c in text:
        if c.isspace() or c.isnumeric():
            cipher += c
        elif c.isupper():
            cipher += chr((ord(c) + shift - 65) % 26 + 65)
        else:
            cipher += chr((ord(c) + shift - 97) % 26 + 97)
    return cipher

text = input("Enter text: ")
shift = 0

while shift < 1 or shift > 25:
    shift = int(input("Enter shift: "))

print(encrypt(text, shift))