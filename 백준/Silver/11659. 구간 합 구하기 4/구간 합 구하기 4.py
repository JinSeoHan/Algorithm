import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + l[i-1]
for i in range(m):
    s, e = map(int, input().split())
    print(dp[e] - dp[s-1])