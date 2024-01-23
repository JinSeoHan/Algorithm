'''
힌트 : 배낭문제와 유사
nums에 들어있는 값을 기준으로 더하는 상황 빼는 상황을 고려
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[0]*(21) for row in range(n+1)]
dp[1][nums[1]] = 1

for i in range(2, n):
    for j in range(21):
        if dp[i-1][j]:
            minusCase = j-nums[i]
            plusCase = j+nums[i]

            if 0 <= minusCase:
                dp[i][minusCase] += dp[i-1][j]
            if plusCase <= 20:
                dp[i][plusCase] += dp[i-1][j]
print(dp[n-1][nums[-1]])