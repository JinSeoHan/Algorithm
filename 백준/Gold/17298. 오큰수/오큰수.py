import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = []
for i, v in enumerate(a):
    if not stack:
        stack.append(i)
        continue
    while stack and a[stack[-1]] < v:
        a[stack.pop()] = v
    stack.append(i)
    
while stack:
    a[stack.pop()] = -1
print(*a)