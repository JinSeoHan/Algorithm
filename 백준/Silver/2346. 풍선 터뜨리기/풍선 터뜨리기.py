import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
l = deque(enumerate(map(int, input().split())))

curr = 0
next = 0

result = []
while l:
    idx, paper = l.popleft()
    result.append(idx + 1)

    if paper > 0:
        l.rotate(-(paper-1))
    elif paper < 0:
        l.rotate(-paper)

print(*result)