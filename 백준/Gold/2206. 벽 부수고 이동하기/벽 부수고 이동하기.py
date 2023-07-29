import sys
from collections import deque
input = sys.stdin.readline

def isValidLocation(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

directions = [(0,1), (1,0), (0,-1), (-1,0)]
def BFS():
    visited[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0))
    while queue:
        x, y, w = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][w]

        for direction in directions:
            nx, ny = x+direction[0], y+direction[1]
            
            if isValidLocation(nx, ny):
                if matrix[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx,ny,w))
                elif matrix[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    queue.append((nx,ny,w+1))
    return -1

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for r in range(N)]
visited = [[[0,0] for c in range(M)] for r in range(N)]

print(BFS())