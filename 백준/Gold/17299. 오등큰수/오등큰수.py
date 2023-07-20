import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))

stack = []
f = {}
for v in l:
    f[v] = f[v] + 1 if v in f else 0

for i, v in enumerate(l):
    while stack and f[v] > f[l[stack[-1]]]:
        l[stack.pop()] = v
    stack.append(i)
while stack:
    l[stack.pop()] = -1
print(*l)