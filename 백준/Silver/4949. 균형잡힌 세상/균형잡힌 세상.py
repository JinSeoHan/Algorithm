import sys
input = sys.stdin.readline

def isPair(a : str, b : str) -> bool:
    result = False
    if a == '(' and b == ')':
        result = True
    elif a == '[' and b == ']':
        result = True
    return result


s = input().rstrip('\n')
stack = []

isPrint = False
while s[0] != '.':
    for c in s:
        if c != '(' and c != ')' and c != '[' and c != ']':
            continue

        if c == '(' or c == '[':
            stack.append(c)
        elif len(stack) != 0 and isPair(stack[-1], c):
            stack.pop()
        else:
            print('no')
            isPrint = True
            break
    if not isPrint:
        if len(stack) != 0:
            print('no')
        else:
            print('yes')
    isPrint = False
    stack = []
    s = input().rstrip('\n')