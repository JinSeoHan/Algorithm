from collections import deque
def isCorrect(arr):
    stack = []
    for i in arr:
        
        if len(stack) == 0 and i in [']', '}', ')']:
            return False
        
        elif i in ['[', '{', '(']:
            stack.append(i)
        elif stack[-1] == '[' and i == ']':
            stack.pop()
        elif stack[-1] == '{' and i == '}':
            stack.pop()
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            return False
    if len(stack) == 0: return True
    else: return False
            
def solution(s):
    queue = deque(s)
    number = len(s)
    cnt = 0
    for i in range(number):
        if isCorrect(queue): 
            cnt += 1
        queue.append(queue.popleft())
    return cnt