import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

stack = []
result = 0
for i, v in enumerate(l):
    count = 1
    while stack and v >= stack[-1][0]:
        if v == stack[-1][0]:
            count += stack[-1][1]
            result += stack[-1][1]
            stack.pop()
        else:
            result += stack.pop()[1]

    if stack:
        result += 1
    
    stack.append([v,count])

print(result)