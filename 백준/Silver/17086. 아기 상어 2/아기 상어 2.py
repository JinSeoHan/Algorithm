import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for row in range(n):
    board.append(list(map(int, input().split())))

def validate(i, j):
    return 0 <= i < n and 0 <= j < m

def bfs():
    while queue:
        ci, cj = queue.popleft()

        for dir in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            ni, nj = ci+dir[0], cj+dir[1]
            if validate(ni, nj) and not board[ni][nj]:
                board[ni][nj] += board[ci][cj] + 1
                queue.append((ni,nj))

queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1: queue.append((i,j))
bfs()
print(max(map(max,board))-1)