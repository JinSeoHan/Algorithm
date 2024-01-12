import sys
input = sys.stdin.readline

t = int(input())
dp = [[0]*4 for row in range(10001)]
dp[1][1] = 1
dp[2][1], dp[2][2] = 1, 1
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1
for i in range(4, 10001):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

for _ in range(t):
    q = int(input())
    result = dp[q][1] + dp[q][2] + dp[q][3]
    print(result)