import sys
from collections import deque
input = sys.stdin.readline

directions = [(0,1), (1,0), (0,-1), (-1,0)]
def BFS():
    while queue:
       x, y = queue.popleft()

       for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            if isValidLocation(nx, ny):
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))

def isValidLocation(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for r in range(N)]
queue = deque()

#익은 배추의 위치를 저장
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append((i,j))

BFS()
maxV = 0
for i in range(N):
    if 0 in matrix[i]:
        print(-1)
        exit(0)
    maxV = max(maxV, max(matrix[i]))
print(maxV - 1)