#f(n) = f(n-2)*f(2) + f(n-4)*2 + ... + f(2)*2 + 2
def solution(n):
    memo = [0]*(n+1)
    memo[2] = 3
    if n % 2 != 0: return 0
    for i in range(4, n+1, 2):
        if i % 2 == 0:
            memo[i] = memo[i-2]*3
            for j in range(i-4, 1, -2):
                memo[i] += memo[j]*2
            memo[i] += 2
            memo[i] = memo[i]%1000000007
            
    print(memo)
    return memo[-1]