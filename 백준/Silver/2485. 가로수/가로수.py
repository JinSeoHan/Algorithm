import sys
from math import gcd

input = sys.stdin.readline
def greatestCommonDivisor(a : int, b : int) -> int:
    big = a
    small = b
    if a < b:
        big = b
        small = a
        
    while small != 0:
        big, small = small, big % small
    return big

n = int(input())
prev = int(input())
lArr = list()
for i in range(n-1):
    curr = int(input())
    lArr.append(curr - prev)
 
    prev = curr

gcd = lArr[0]
for i in range(1,len(lArr)):
    gcd = greatestCommonDivisor(gcd, lArr[i])

count = 0
for i in lArr:
    count += i // gcd - 1

print(count)