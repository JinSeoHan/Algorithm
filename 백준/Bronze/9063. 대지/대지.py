import sys
x = []
y = []
N = int(input())
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
print((max(x) - min(x)) * (max(y) - min(y)))