'''
힌트 : 팰린드롬 양 끝에 같은 수를 붙이면 그 수 또한 팰린드롬이다.

ex) 
'121' -> 팰린드롬
4'121'4 -> 동일하게 팰린드롬

f(s, e) : s번 수에서 e번 까지의 수는 팰린드롬인가? (0 or 1)

f(s, e) = ( v(s) == v(e) ) and f(s+1, e-1)
==> s와 e가 동일하면서 f(s+1, e-1)이 팰린드롬이면? f(s,e)도 팰린드롬이다.
'''
import sys
input = sys.stdin.readline

n = int(input())
v = [0] + list(map(int, input().split()))

dp = [[0]*(n+1) for s in range(n+1)]

# case1 : diff <= 1
for diff in range(2):
    for s in range(1,n-diff+1):
        e = s+diff
        if v[s] == v[e]: dp[s][e] = 1

# case2 : diff > 1
for diff in range(2, n):
    for s in range(1, n-diff+1):
        e = s+diff
        if v[s] == v[e] and dp[s+1][e-1]: dp[s][e] = 1

for t in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s][e])