import math
def solution(n, k):
    nums = list(range(1, n+1))
    k -=1 #index로바꿔줌
    stack=[]
    while nums:
        v = k // math.factorial(n-1)
        stack.append(nums[v])
        del nums[v]
        k %= math.factorial(n-1)
        n -= 1
    return stack
       
