import sys
input = sys.stdin.readline

primeList = [2, 3]

def isPrime(num : int) -> int:
    root = int(num**(1/2))
    if num < 2:
        return False
    
    for i in range(2, root+1):
        if num % i == 0:
            return False  
             
    return True

def greaterPrime(a : int) -> int:
    num = a
    
    while True:
        if isPrime(num):
            return num
        num += 1

n = int(input())
for i in range(n):
    a = int(input())
    print(greaterPrime(a))