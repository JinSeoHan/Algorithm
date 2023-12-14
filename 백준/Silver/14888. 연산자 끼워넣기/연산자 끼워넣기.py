import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))#수
opers = list(map(int, input().split()))#연산자별 개수

maxNum, minNum = -10**15, 10**15
def dfs(idx, s, plus, minus, mul, div):
    global maxNum, minNum
    if idx == n-1:
        maxNum = max(maxNum, s)
        minNum = min(minNum, s)
        return
    
    if plus:
        dfs(idx+1, s + nums[idx+1], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, s - nums[idx+1], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, s * nums[idx+1], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, int(s / nums[idx+1]), plus, minus, mul, div-1)

dfs(0, nums[0], opers[0], opers[1], opers[2], opers[3])
print(maxNum)
print(minNum)