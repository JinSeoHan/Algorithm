import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

s = sum(c)
dp = [[0]*(s+1) for r in range(N+1)]

for i in range(N+1):
    for j in range(s+1):
        if j-c[i] < 0:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j-c[i]]+m[i],dp[i-1][j])

for i,v in enumerate(dp[-1]):
    if v >= M:
        print(i)
        break