import sys
input = sys.stdin.readline

r, s = map(int, input().split())
board = [list(input()) for _ in range(r)] # 운석의 위치정보

# 운석이 맞닿을 위치까지의 offset을 찾는다.
offset = 5000
for j in range(s):
    flagA, flagB = False, False
    topGround, bottomMeteor = 5000, -1
    for i in range(r):
        if board[i][j] == 'X':
            bottomMeteor = max(bottomMeteor, i)
            flagA = True
        if board[i][j] == '#':
            topGround = min(topGround, i)
            flagB = True
    newOffset = topGround - bottomMeteor - 1
    if flagA and flagB:
        offset = min(offset,newOffset)

# 복원한 사진을 그린다.
newBoard = [['.']*s for _ in range(r)]
for i in range(r):
    for j in range(s):
        if board[i][j] == 'X':
            newBoard[i+offset][j] = 'X'
        if board[i][j] == '#':
            newBoard[i][j] = '#'

for i in range(r):
    for j in range(s):
        sys.stdout.write(newBoard[i][j])
    sys.stdout.write('\n')