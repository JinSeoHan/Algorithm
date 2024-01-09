import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(map(int, input().split()))

dp = [0]*(n+2)
m = 0
# 역으로 검사하면서 최대수입을 저장
for i in range(n-1, -1, -1):
    t, p = l[i]
    if i+t > n: 
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t] + p)

print(dp[0])