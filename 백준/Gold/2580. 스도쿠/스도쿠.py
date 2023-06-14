import sys
input = sys.stdin.readline

def sudoku(posIdx : int):
    if posIdx == len(spotL):
        for i in range(9):
            print(*board[i])
        exit()

    for i in range(1, 10):
        pos = spotL[posIdx]
        if isPos(pos, i):
            board[pos[0]][pos[1]] = i
            sudoku(posIdx+1)
            board[pos[0]][pos[1]] = 0

def isPos(pos : tuple, num : int):

    x = pos[0]
    y = pos[1]

    for i in range(9):
        if board[x][i] == num:
            return False

    for i in range(9):
        if board[i][y] == num:
            return False

    diffX = x // 3 * 3
    diffY = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[diffX + i][diffY + j] == num:
                return False
    
    return True

board = []
spotL = []

for i in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            spotL.append((i,j))

sudoku(0)