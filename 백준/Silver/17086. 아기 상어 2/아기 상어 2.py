import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for row in range(n):
    board.append(list(map(int, input().split())))

def validate(i, j):
    return 0 <= i < n and 0 <= j < m

def bfs(i, j):
    queue = deque()
    queue.append((i,j,0))
    visited = [[False]*m for row in range(n)]

    while queue:
        ci, cj, cDist = queue.popleft()

        for dir in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            ni, nj = ci+dir[0], cj+dir[1]

            if validate(ni, nj) and not visited[ni][nj]:
                if board[ni][nj] == 1:
                    return cDist + 1
                queue.append((ni,nj,cDist+1))
                visited[ni][nj] = True

result = 0
for i in range(n):
    for j in range(m):
        if not board[i][j]: result = max(result, bfs(i,j))

print(result)