'''
힌트 : 뒤에서부터 값을 넣어야함
dp[i] : i번째 이름을 새로운 라인으로 만들어서 (i+1)~n까지 이름을 새롭게 만들어진 라인에 하나씩 넣어보면서 찾은 최솟값
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [0] + [int(input()) for i in range(n)]

dp = [10000000]*(n+1)
dp[n] = 0
for i in range(n-1, 0, -1):
    newLine = m-nums[i]
    dp[i] = newLine**2 + dp[i+1]
    # i~(n-1)번째 이름을 순서대로 새로운 라인에 추가해 보면서 제곱의 합의 최솟값을 찾음
    for j in range(i+1, n+1):
        newLine -= nums[j] + 1
        # j번째 이름을 새로운 라인에 추가할 때 칸의 개수를 넘지 않을 경우에만 처리
        if newLine >= 0:
            # 마지막 이름까지 들어갈 수 있는 경우 
            if j == n: 
                dp[i] = 0
                break
            dp[i] = min(dp[i], newLine**2 + dp[j+1])
        # 칸 개수를 넘는 경우 최솟값을 찾은 것으로 판단
        else: break
    
print(dp[1])