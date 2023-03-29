N = int(input())
count = 0
for _ in range(N):
    stack = ['_']
    result = True
    s = input()
    for i in s:
        if stack[-1] == i:
            stack.append(i)
            continue
        elif i in stack:
            result = False
            break
        stack.append(i)
    if result: count += 1
print(count)