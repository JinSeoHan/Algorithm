import sys
input = sys.stdin.readline

def isTopMatch(stack, bomS):
    stackIdx = len(stack) - len(bomS)
    for i in range(len(bomS)):
        if stackIdx < 0 or bomS[i] != stack[stackIdx]:
            return False
        stackIdx += 1
    return True

word = input().strip()
bomS = input().strip()

stack = []
for v in word:
    stack.append(v)
    if stack[-1] == bomS[-1]:
        if isTopMatch(stack, bomS):
            for _ in range(len(bomS)):
                stack.pop()

print(''.join(stack)) if stack else print("FRULA")