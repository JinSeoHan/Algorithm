import sys
input = sys.stdin.readline

n = int(input())
h = [0] + [int(input()) for i in range(n)] + [0]

stack = []
result = 0
for i, v in enumerate(h):
    while stack and v < h[stack[-1]]:
        standidx = stack.pop()
        high = h[standidx]
        result = max(result, high*(i-stack[-1]-1))
    stack.append(i)
print(result)