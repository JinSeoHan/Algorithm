import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [10001]*(k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1) # coin을 더해서 만들 수 있는 최소값을 찾은 후 기존보다 더 작으면 업데이트
print(-1) if dp[k] == 10001 else print(dp[k])