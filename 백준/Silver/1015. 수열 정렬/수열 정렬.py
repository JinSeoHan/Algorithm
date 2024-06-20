from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = deque(map(int, input().split()))

p = list(enumerate(sorted(a)))

result = []
while p:
    target = a.popleft()

    for i in range(len(p)):
        o, v = p[i]
        if target == v:
            result.append(o)
            del p[i]
            break
print(*result)