import sys
input = sys.stdin.readline

n = int(input())
l = [0] * (n+1)
for i in range(2, n+1):
    m = l[i-1]
    if i % 2 == 0:
        m = min(m, l[i//2])
    if i % 3 == 0:
        m = min(m, l[i//3])
    l[i] = m + 1
print(l[n])