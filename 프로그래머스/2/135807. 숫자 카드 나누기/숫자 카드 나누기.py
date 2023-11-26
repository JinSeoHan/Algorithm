import math
def solution(arrayA, arrayB):
    result = 0


    gcdA = arrayA[0]
    for a in arrayA:
        gcdA = math.gcd(gcdA,a)
    gcdB = arrayB[0]
    for b in arrayB:
        gcdB = math.gcd(gcdB,b)
    
    flag = True
    for b in arrayB:
        if b % gcdA == 0:
            flag = False
            break
    if flag: result = max(result, gcdA)

    flag = True
    for a in arrayA:
        if a % gcdB == 0:
            flag = False
            break
    if flag: result = max(result, gcdB)

    return result