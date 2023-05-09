import sys
input = sys.stdin.readline

def gcd(a: int, b: int) -> int:

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
    return gcd(small, r)

a, b = map(int, input().split())
gcd = gcd(a, b)
print(gcd * (a//gcd) * (b//gcd))