import sys
input = sys.stdin.readline

n = int(input())
mtxInfos = [(0,0)] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for r in range(n+1)]

for gap in range(1, n):
    s = 1
    e = s + gap
    while e <= n:
        dp[s][e] = 10000000000
        for i in range(s, e):
            dp[s][e] = min(dp[s][e], dp[s][i] + dp[i+1][e] + mtxInfos[s][0] * mtxInfos[i+1][0] * mtxInfos[e][1])
        s += 1
        e = s + gap
print(dp[1][n])