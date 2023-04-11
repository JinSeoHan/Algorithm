import sys
a, b, c = sorted(map(int, sys.stdin.readline().split()))
print(2*a+2*b-1) if c >= a + b else print(a+b+c)