import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [1] + [0] * (k+1)
for _ in range(n):
    coin = int(input())
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]
print(dp[k])