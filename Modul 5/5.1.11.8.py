def anagram(str1,str2):
    if str1 == '' or str2 == '':
      return "Not anagram"
      
    str1 = str1.lower()
    str2 = str2.lower()
    
    list1 = list(str1)
    list1.sort()

    list2 = list(str2)
    list2.sort()
    
    return "Anagram" if list1 == list2 else "Not anagram"

str1 = input("string 1 : ")
str2 = input("string 2 : ")
print(anagram(str1,str2))