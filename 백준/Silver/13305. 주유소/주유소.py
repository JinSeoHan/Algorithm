import sys
input = sys.stdin.readline

n = int(input())
e = list(map(int, input().split()))
v = list(map(int, input().split()))

c = v[0] * e[0]
keep = v[0]
for i in range(1, n-1):
    if v[i] < keep:
        c += v[i] * e[i]
        keep = v[i]
    else:
        c += keep * e[i]
print(c)