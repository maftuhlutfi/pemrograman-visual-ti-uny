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

file.close()

try:
    file = open(filename + '.hist', 'w')
except:
    print("Cannot open file.")
    exit()

for key, val in sorted(data.items(), key = lambda k: k[1], reverse = 1):
    print(key, '->', val)
    file.write(key + ' -> ' + str(val) + '\n')

file.close()