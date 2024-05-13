import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(19)]

def isBound(i, j):
    return 0 <= i < 19 and 0 <= j < 19
def isVictory(i, j):
    target = board[i][j] 
    isSuccess = False

    for dir in [(1,0),(1,1),(0,1),(-1,1)]:# 남, 남서, 동, 북동
        for diff in range(6):
            currI, currj = i+dir[0]*diff, j+dir[1]*diff
            if not isBound(currI, currj) or board[currI][currj] != target: break
            isSuccess = True if diff == 4 else False
        if isSuccess:
            if isBound(i-dir[0], j-dir[1]) and board[i-dir[0]][j-dir[1]] == target:
                isSuccess = False
                continue
            return True
    return False

for i in range(19):
    for j in range(19):
        if board[i][j] and isVictory(i, j):
            print(board[i][j])
            print(i+1, j+1)
            exit(0)
print(0)