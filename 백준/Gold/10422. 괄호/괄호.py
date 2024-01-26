'''
dp[6] = dp[4] * (dp[0]) + dp[2] * (dp[2]) + dp[0] * (dp[4])

ex)
2 : ()
4 : ()('') / ''(())
6 : ()()('') (())('') / ()(()) / ''(()()) ''((()))
'''
import sys
input = sys.stdin.readline

t = int(input())

dp = [0]*(5001)
dp[0], dp[2] = 1, 1
for i in range(4, 5001, 2):
    for j in range(i-2, -1, -2):
        dp[i] += dp[j]* dp[i-2-j]
        dp[i] %= 1000000007
for _ in range(t):
    print(dp[int(input())])