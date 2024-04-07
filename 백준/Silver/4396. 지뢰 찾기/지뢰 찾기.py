n = int(input())
board = [[0]*n for r in range(n)]

# x, y 위치 주위 8칸에 지뢰 정보 업데이트
def recordMineCnt(board, x, y):
    for i in [-1, 0, 1]:
        if not (0 <= x+i < n): continue
        for j in [-1, 0, 1]:
            if not (0 <= y+j < n) or board[x+i][y+j] == '*': continue
            board[x+i][y+j] += 1

# 지뢰 정보 기록
mineInfo = []
for i in range(n):
    for j, v in enumerate(list(input())):
        if v == '.': continue
        if v == '*': mineInfo.append((i,j))
        board[i][j] = v
        recordMineCnt(board, i, j)

# 열린칸 지정
isMineDetected = False
for i in range(n):
    for j, v in enumerate(list(input())):
        if v == 'x': 
            if board[i][j] == '*': isMineDetected = True
            continue
        board[i][j] = v

# 지뢰를 밟은 경우 모든 지뢰 오픈
if isMineDetected:
    for i,j in mineInfo:
        board[i][j] = '*'

for r in board:
    for v in r:
        print(v, end='')
    print()