allNum = 247000

isPrimeArr = [True] * allNum

isPrimeArr[0] = False
isPrimeArr[1] = False
for i in range(2, allNum):
    if isPrimeArr[i]:
        j = 2
        # i*j 2*2 2*3 2*4 ... < allNum
        while i * j < allNum:
            isPrimeArr[i*j] = False
            j += 1

n = int(input())
while n != 0:
    count = 0
    for i in range(n+1, 2*n+1):
        if isPrimeArr[i]:
            count += 1
    print(count)
    n = int(input())