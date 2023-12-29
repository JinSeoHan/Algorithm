import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

cnt = 0
def dfs(currDir, r, c):
    result = 0
    if (r, c) == (n-1, n-1):
        return 1
    
    #대각선으로 이동
    if r+1 < n and c+1 < n:
        flag = True
        for dir in [(1,1),(1,0),(0,1)]:
            nr, nc = r+dir[0], c+dir[1]
            if matrix[nr][nc] == 1: 
                flag = False
                break
        if flag : result += dfs(2, r+1, c+1)

    # 가로 대각선 => 가로이동
    if currDir in (1, 2) and c+1 < n and matrix[r][c+1] == 0:
        result += dfs(1, r, c+1)
    
    # 세로 대각선 => 세로이동
    if currDir in (2, 3) and r+1 < n and matrix[r+1][c] == 0:
        result += dfs(3, r+1, c)
    return result
print(dfs(1, 0, 1))