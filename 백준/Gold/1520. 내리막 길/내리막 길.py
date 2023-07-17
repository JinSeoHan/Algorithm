import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for rP in rp:
            if 0 <= x+rP[0] < m and 0 <= y+rP[1] < n and l[x+rP[0]][y+rP[1]] < l[x][y]:
                dp[x][y] += dfs(x+rP[0], y+rP[1])
    return dp[x][y]

m, n = map(int, input().split())
l = [list(map(int, input().split()))for r in range(m)]
dp = [[-1]*n for r in range(m)]
rp = [(0, 1), (1, 0), (0, -1), (-1,0)]

print(dfs(0,0))