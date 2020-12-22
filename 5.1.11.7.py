def isPalindrome(str):
    str = str.replace(" ", "")
    str = str.lower()
    rev = str[::-1]
    return "It's a palindrome" if str == rev else "It's not a palindrome"

str = input("Enter text: ")
print(isPalindrome(str))