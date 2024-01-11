import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,k = map(int, input().split())

board = [[False]*m for row in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = True

def validate(r, c):
    return 0 <= r < n and 0 <= c < m

def dfs(r, c, visited, board):
    visited[r][c] = True
    cnt = 0

    for dir in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr, nc = r + dir[0], c + dir[1]
        if validate(nr,nc) and board[nr][nc] == True and not visited[nr][nc]:
            cnt += dfs(nr, nc, visited, board)
    return cnt + 1

visited = [[False]*m for row in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == True:
            result = max(result, dfs(i, j, visited, board))
print(result)