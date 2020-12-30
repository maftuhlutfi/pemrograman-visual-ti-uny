def findWord(str1, str2):
    for c in str1:
        if str2.find(c) < 0:
            return "No"
    return "Yes"
    
str1 = input("String 1: ")
str2 = input("String 2: ")
print(findWord(str1,str2))