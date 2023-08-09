import sys
input = sys.stdin.readline

N = int(input())
isPrime = [True] * (N+1)
isPrime[1] = False
prime = []

def findPrime():

    for i in range(1, N+1):
        if not isPrime[i]:
            continue
        prime.append(i)

        cnt = 2
        while i*cnt <= N:
            isPrime[i*cnt] = False
            cnt += 1

findPrime()

l, r = -1, -1
sum = 0
result = 0
primeLength = len(prime)
while r < primeLength:

    if sum < N:
        r += 1
        if r < primeLength:
            sum += prime[r]
    else:
        if sum == N:
            result += 1
        l += 1
        sum -= prime[l]

print(result)