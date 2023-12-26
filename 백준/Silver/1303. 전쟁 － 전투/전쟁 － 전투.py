import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

matrix = []
for i in range(m):
    matrix.append(list(input().rstrip()))

def isValid(r, c):
    return 0 <= r < m and 0 <= c < n

def dfs(matrix, cr, cc, visited, target):
    if not isValid(cr, cc) or visited[cr][cc] or matrix[cr][cc] != target: return 0
    visited[cr][cc] = True


    result = 0
    for pos in [(1,0),(0,1),(-1,0),(0,-1)]:
        nr, nc = cr+pos[0], cc+pos[1]
        result += dfs(matrix, nr, nc, visited, target)
    return result + 1

visited = [[False]*n for i in range(m)]

answer = [0, 0]
for row in range(m):
    for col in range(n):
        if not visited[row][col]:
            N = dfs(matrix, row, col, visited, matrix[row][col])
            if matrix[row][col] == 'W':
                answer[0] += N**2
            else:
                answer[1] += N**2

print(*answer)