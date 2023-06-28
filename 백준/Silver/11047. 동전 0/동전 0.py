import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = []
for i in range(n):
    v.append(int(input()))
count = 0
for i in range(n-1, -1, -1):
    if k >= v[i]:
        count += k // v[i]
        k %= v[i]
print(count)