import sys
input = sys.stdin.readline

memo = [0, 1, 1, 1, 2]
memo += [None] * 100


def dp(num):
    if memo[num] != None:
        return memo[num]

    memo[num] = dp(num-1) + dp(num-5)
    return memo[num]

for i in range(int(input())):
    print(dp(int(input())))