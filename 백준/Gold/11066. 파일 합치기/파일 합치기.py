'''
힌트 : 행렬 곱셈 순서(113128) 문제와 비슷하게 접근

dp[i][j]: i번파일부터 j번파일까지 합칠 때 드는 최소비용

dp(s, e) = s~e파일합cost + dp(s, i) + dp(i+1, e) # (s <= i < e)
'''
import sys
input = sys.stdin.readline

def getMinimumJoinCost():
    dp = [[0]*(k+1) for i in range(k+1)]

    for diff in range(1, k):
        for s in range(1, k-diff+1):
            e = s+diff
            dp[s][e] = 1000000000000
            for i in range(s, e):
                dp[s][e] = min(dp[s][e], arr[e]-arr[s-1]+dp[s][i]+dp[i+1][e])
    return dp[1][k]

for _ in range(int(input())):
    k = int(input())
    nums = [0] + list(map(int,input().split()))

    # 누적합
    arr= []
    arr.append(nums[0])
    for num in nums[1:]:
        arr.append(arr[-1]+num)

    print(getMinimumJoinCost())