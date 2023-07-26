import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

queue = deque()
directions = [(0,1), (1,0), (0,-1), (-1,0)]
def BFS(x, y):
    for direction in directions:
        nX, nY = x + direction[0], y + direction[1]
        if isValidLocation(nX, nY):
            if maze[nX][nY] == 1 and (nX, nY) != (0, 0):
                queue.append((nX, nY))
                maze[nX][nY] = maze[x][y] + 1
            if maze[nX][nY] > 1:
                order = min(maze[nX][nY], maze[x][y] + 1)
                maze[nX][nY] = order
    while queue:
        loc = queue.popleft()
        BFS(loc[0], loc[1])

def isValidLocation(x, y):
    if 0 <= x < N and 0 <= y <M:
        return True
    return False

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for r in range(N)]


BFS(0,0)
print(maze[-1][-1])