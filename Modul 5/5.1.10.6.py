representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('#', '#', '#', '#', '#'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('  ', '  ', '  ', '  ', ' #'),
}

def segment7(number):
    digits = [representations[digit] for digit in number]
    for i in range(5):
        print(" ".join(segment[i] for segment in digits))
        
number = input("Enter number: ")
while len(number) < 0:
    number = input("Enter number: ")
    
segment7(number)