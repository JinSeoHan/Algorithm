from collections import deque
import sys
input = sys.stdin.readline

S = input().strip()

flag = False
stack = deque()
for s in S:
    if s == ' ':
        print(''.join(stack), end=' ')
        stack.clear()
        continue

    if s == '<' or flag:
        if stack: 
            print(''.join(stack),end='')
            stack.clear()
        flag = True
        print(s, end='')
        if s == '>': flag = False
        continue

    stack.appendleft(s)
if stack: print(''.join(stack), end='')