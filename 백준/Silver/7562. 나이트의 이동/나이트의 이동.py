import sys
from collections import deque
input = sys.stdin.readline

def isValidLocation(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

directions = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
queue = deque()
def BFS(x, y):
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        if (x, y) == v:
            return board[x][y]

        for direction in directions:
            nX, nY = x + direction[0], y + direction[1]
            if isValidLocation(nX, nY):
                if (nX,nY) != u and board[nX][nY] == 0:
                    board[nX][nY] = board[x][y] + 1
                    queue.append((nX, nY))

for testCount in range(int(input())):
    n = int(input())
    u, v = tuple(map(int, input().split())), tuple(map(int, input().split()))
    board = [[0]*n for r in range(n)]
    
    print(BFS(u[0], u[1]))
    queue.clear()