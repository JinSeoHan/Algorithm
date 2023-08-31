def solution(n):
    nextN = n+1
    while str(bin(n)).count('1') != str(bin(nextN)).count('1'):
        nextN += 1
    return nextN