'''
memoization을 활용한 백트레킹
dp[a][b][c][pre][prepre]
 : A의 개수 a B의 개수 b C의 개수 c를 사용하면서 B와 C값이 이전값(pre)와 전전값(prepre) 조건을 만족하는 경우를 방문했는지
 result[i]: i번째로 출근한 사람의 이름
'''
from collections import Counter
import sys
input = sys.stdin.readline

s = input().rstrip()
count = Counter(s)
result = ['']*len(s)
dp = [[[[[False]*3 for pre in range(3)] for c in range(len(s))] for b in range(len(s))] for a in range(len(s))]
A,B,C = 0, 1, 2

def dfs(a, b, c, pre, prepre):
    if (a,b,c) == (count['A'],count['B'],count['C']):
        print(''.join(result))
        exit(0)
    if dp[a][b][c][pre][prepre]: return False
    
    dp[a][b][c][pre][prepre] = True

    # 여분의 A값이 남아 있다면
    if a < count['A']:
        result[a+b+c] = 'A'
        if dfs(a+1, b, c, A, pre): return True
    # 여분의 B값이 남아 있다면
    if b < count['B']:
        result[a+b+c] = 'B'
        if pre != B:
            if dfs(a, b+1, c, B, pre): return True
    # 여분의 C값이 남아 있다면
    if c < count['C']:
        result[a+b+c] = 'C'
        if pre != C and prepre != C:
            if dfs(a, b, c+1, C, pre): return True
    return False

dfs(0,0,0,0,0)
print(-1)