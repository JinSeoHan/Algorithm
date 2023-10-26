from itertools import permutations
def solution(numbers):
    memo = set()
    result = 0
    for i in range(1, len(numbers)+1):
        for num in list(permutations(numbers, i)):
            num = int(''.join(num))
            if num in memo: continue
            memo.add(num)
            if isPrime(num):
                result += 1
    return result
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True