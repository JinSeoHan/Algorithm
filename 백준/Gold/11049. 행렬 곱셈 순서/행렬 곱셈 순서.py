'''
dp[i][j] : i번째 행렬에서 j번째 행렬까지의 곱셈 연산 횟수의 최솟값
f(a, b) : 행렬 a부터 b까지 곱셈 연산 횟수 최솟값

힌트 : 행렬의 곱은 두 부분 행렬의 곱으로 이루어져있다는 특징을 활용

    (A X B) X (C X D) == a*d*e + (AXB)결과 + (CXD)결과
r   'a'   b   c    d
c    b    c  'd'  'e'
'''
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for row in range(n)]
for diff in range(1, n):
    for s in range(n-diff):
        e = s+diff
        dp[s][e] = 2**31
        for k in range(s, e):
            dp[s][e] = min(dp[s][e], matrix[s][0]*matrix[k][1]*matrix[e][1] + dp[s][k] + dp[k+1][e])
print(dp[0][n-1])