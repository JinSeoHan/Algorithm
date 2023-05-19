import sys
input = sys.stdin.readline

n = int(input())
stack = []
isDecision = False
for i in range(n):
    s = input().rstrip('\n')

    for c in s:
        if len(stack) == 0 and c == ')':
            print('NO')
            isDecision = True
            break
        
        if c == '(':
            stack.append(c)
        else:
            stack.pop()
    if not isDecision:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    stack = []
    isDecision = False