import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

directions = [(0,1), (1,0), (0,-1), (-1,0)]
def DFS(x, y):
    visited[x][y] = True

    for spot in directions:
        nX, nY = x + spot[0], y + spot[1]
        if isValidLocation(nX, nY):
            if not visited[nX][nY] and field[nX][nY] == 1:
                DFS(nX, nY)

def isValidLocation(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0

    for __ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                DFS(i,j)
                count += 1
    print(count)