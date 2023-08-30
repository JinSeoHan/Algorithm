def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')': return False
        stack.append('(') if i == '(' else stack.pop()
    return len(stack) == 0    