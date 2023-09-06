from collections import deque
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a,b)
    
def solution(arr):
    a = arr[0]
    for i in arr:
        a = lcm(a, i)
    print(a)
    return a