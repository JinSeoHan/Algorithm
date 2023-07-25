import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

perimeters = [(0,1), (1,0), (0,-1), (-1,0)]
def DFS(s, e):
    global count

    count += 1
    visited[s][e] = True

    for spot in perimeters:
        nX, nY = s + spot[0],e + spot[1]
        if isEnableLocation(nX, nY):
            if not visited[nX][nY] and arr[nX][nY] == '1':
                DFS(nX, nY)

def isEnableLocation(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

n = int(input())
arr = [list(input().rstrip()) for r in range(n)]
visited = [[False]*n for r in range(n)]
count = 0

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            DFS(i,j)
            result.append(count)
            count = 0
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])