class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self):
        self.args = "Bad line encountered."

class FileEmpty(StudentsDataException):
    def __init__(self):
        self.args = "File is empty."

filename = input('Enter file name: ')

try:
    f = open(filename, 'r')
    content = f.read()

    data = {}

    if len(content) == 0:
        raise FileEmpty()
    
    for row in content.split('\n'):
        columns = [column for column in row.split('\t')]

        if len(columns) != 3:
            raise BadLine()

        fullName = columns[0] + ' ' + columns[1]
        points = columns[2]

        if fullName not in data.keys():
            data[fullName] = float(points)
        else:
            data[fullName] += float(points)

    for key, val in data.items():
        print(key, '\t', val)

except FileEmpty as fe:
    print(''.join(fe.args))
except BadLine as bl:
    print(''.join(bl.args))

