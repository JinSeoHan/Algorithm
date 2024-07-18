n = int(input())
memo = [0]*(n+1)
for v in range(1, n+1):
    for i in range(2, v+1):
        if v < i: break
        while v % i == 0:
            memo[i] += 1
            v /= i
print(0) if n < 5 else print(min(memo[2], memo[5]))