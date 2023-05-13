import sys
input = sys.stdin.readline

allNum = 1000001

isPrimeArr = [True] * allNum

isPrimeArr[0] = False; isPrimeArr[1] = False
for i in range(2, allNum):#모든 소수를 찾음

    if isPrimeArr[i]:
        j = 2
        while i*j < allNum:
            isPrimeArr[i*j] = False
            j += 1

def goldbachPartitions(a : int) -> int:
    count = 0
    for i in range(2, a//2+1):
        if isPrimeArr[i] and isPrimeArr[a-i]:
            count += 1
    return count


n = int(input())

for _ in range(n):
    num = int(input())
    print(goldbachPartitions(num))