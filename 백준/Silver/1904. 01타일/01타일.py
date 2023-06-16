import sys
input = sys.stdin.readline

n = int(input())
sum = 1
memo = [0,1,2]
if not (n < 3): 
    for i in range(3, n+1):
            memo[0], memo[1], memo[2] = memo[1], memo[2], (memo[1] + memo[2]) % 15746  
print(memo[n]) if n < 3 else print(memo[2])