import sys
input = sys.stdin.readline

one = 101
two = 101
three = 101 
memo = [[[None for k in range(three)] for j in range(two)] for i in range(one)]

def w(a, b, c):
    if memo[a][b][c] != None:
            return memo[a][b][c]
    
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        memo[a][b][c] =  w(20, 20, 20)
        return memo[a][b][c]
    
    elif a < b and b < c:
        memo[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]
    
    else:
        memo[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]


nums = list(map(int, input().split()))
while not (nums[0] == -1 and nums[1] == -1 and nums[2] == -1):
    print(f'w({nums[0]}, {nums[1]}, {nums[2]}) = {w(nums[0], nums[1], nums[2])}')
    nums = list(map(int, input().split()))