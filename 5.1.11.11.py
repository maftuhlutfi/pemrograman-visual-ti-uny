def createBoard():
    board = [[-1 for i in range(9)] for j in range(9)]
    for i in range(9):
        print('Line', i + 1, end='')
        line = input(': ')
        for j in range(9):
            board[i][j] = int(line[j])
    return board  

def checkSudoku(board):
    # Validate line
    for line in board:
      if not checkValidLine(line):
        return "No"
    
    # Validate row
    for i in range(9):
      row = [-1 for x in range(9)]
      for j in range(9):
        row[j] = board[j][i]
      if not checkValidRow(row):
        return "No"

    # Validate square
    for i in range(9):
      square = [-1 for x in range(9)]
      for j in range(9):
        square[j] = board[j//3][j%3]
      if not checkValidSquare(square):
        return "No"

    return "Yes"

def checkValidLine(line):
    lineSet = set(line)
    line = list(lineSet)
    return len(line) == 9
    
def checkValidRow(row):
    rowSet = set(row)
    row = list(rowSet)
    return len(row) == 9

def checkValidSquare(square):
    squareSet = set(square)
    square = list(squareSet)
    return len(square) == 9

board = createBoard()
print(checkSudoku(board))