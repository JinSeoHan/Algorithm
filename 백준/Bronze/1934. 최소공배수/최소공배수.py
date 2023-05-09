import sys
input = sys.stdin.readline
def f(a, b):
    big = 0
    small = 0
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    r = big % small
    
    if r == 0:
        return small

    return f(small, r)

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    gcb = f(a, b)
    print(gcb * (a//gcb) * (b//gcb))