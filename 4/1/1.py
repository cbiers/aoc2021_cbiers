def checkBingo(board, numbers):
    for i in range(5):
        if(board[i][0] in numbers and board[i][1] in numbers and board[i][2] in numbers and board[i][3] in numbers and board[i][4] in numbers):
            return True
        if(board[0][i] in numbers and board[1][i] in numbers and board[2][i] in numbers and board[3][i] in numbers and board[4][i] in numbers):
            return True
    if(board[0][0] in numbers and board[1][1] in numbers and board[2][2] in numbers and board[3][3] in numbers and board[4][4] in numbers):
        return True
    if(board[4][0] in numbers and board[3][1] in numbers and board[2][2] in numbers and board[1][3] in numbers and board[0][4] in numbers):
        return True
    return False

def boardValue(board, numbers):
    res = 0
    for line in board:
        for n in line:
            if n not in numbers:
                res += (int)(n)
    return res


f = open("in.txt", "r")
lines = f.readlines()

draw = lines[0].split(",")
boards = [[]]

lineCount = 0
boardCount = 0

for line in lines[2:]:
    if lineCount == 5:
        lineCount = 0
        boardCount += 1
        boards.append([])
    else:
        boards[boardCount].append(line.split())
        lineCount += 1

win = False
res = 0

for i in range(len(draw)):
    if win:
        break
    for board in boards:
        if checkBingo(board, draw[:i+1]):
            res = int(draw[i]) * boardValue(board, draw[:i+1])
            win = True
            break

print res
