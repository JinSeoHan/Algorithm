import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (d*c-a*f)//(b*d-e*a)
print(x, y)