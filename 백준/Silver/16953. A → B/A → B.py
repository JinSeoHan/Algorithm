import sys
from collections import deque
input = sys.stdin.readline

a, b = input().split()

def bfs():
    queue = deque()
    queue.append((a,1))

    while queue:
        cv, cnt = queue.popleft()

        for nv in [str(int(cv)*2), cv+'1']:
            if nv == b:
                return cnt+1
            if int(nv) < int(b):
                queue.append((nv, cnt+1))
    return -1

print(bfs())
