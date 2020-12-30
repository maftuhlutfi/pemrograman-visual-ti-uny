filename = input('Enter filename: ')

try:
    file = open(filename, "rt")
except:
    print("Cannot open file.")
    exit()

content = file.read()
data = {}

for ch in content:
    if ch.isalpha():
        chlower = ch.lower()
        if chlower in data.keys():
            data[chlower] += 1
        else:
            data[chlower] = 1
    
for key, val in sorted(data.items()):
    print(key, '->', val)