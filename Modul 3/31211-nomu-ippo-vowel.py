wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable
userWord = input("Enter a word: ").upper()

for char in userWord:
    # Complete the body of the loop.
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        continue
    else:
        wordWithoutVovels += char

# Print the word assigned to wordWithoutVowels.
print(wordWithoutVovels)