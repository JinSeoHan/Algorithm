import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(input().rstrip()))

def isValid(r, c):
    return 0 <= r < n and 0 <= c < n
def getRowCnt(r, c):
    cnt = 1
    # (r,c) 기준 오른쪽
    for i in range(c+1, n):
        if board[r][c] == board[r][i]:
            cnt += 1
        else:break
    # (r,c) 기준 왼쪽
    for i in range(c-1, -1, -1):
        if board[r][c] == board[r][i]:
            cnt += 1
        else:break
    return cnt
def getColCnt(r, c):
    cnt = 1
    # (r, c) 기준 아래
    for i in range(r+1, n):
        if board[r][c] == board[i][c]:
            cnt += 1
        else:break
    # (r, c) 기준 위
    for i in range(r-1, -1, -1):
        if board[r][c] == board[i][c]:
            cnt += 1
        else:break
    return cnt

    
# (r, c) 위치 기준으로 행과 열에서 최대값을 찾음
def getCandyCnt(r, c):
    rCnt = getRowCnt(r, c)
    cCnt = getColCnt(r, c)
    return max(rCnt, cCnt)

result = 0
for i in range(n):
    for j in range(n):
        # 4방향으로 이동
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = i + dir[0], j + dir[1]
            if isValid(ni,nj):
                board[i][j] , board[ni][nj] = board[ni][nj], board[i][j]
                result = max(result, getCandyCnt(ni, nj))
                board[i][j] , board[ni][nj] = board[ni][nj], board[i][j]
print(result)