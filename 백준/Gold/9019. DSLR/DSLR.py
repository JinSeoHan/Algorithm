import sys 
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n1, n2 = map(int, input().split())

    queue = deque()
    queue.append((n1, ''))
    visited = set()
    visited.add(n1)
    while queue:
        cValue, cmd = queue.popleft()
        if cValue == n2:
            break

        nV = cValue * 2 % 10000
        if nV not in visited:
            queue.append((nV, cmd + 'D'))
            visited.add(nV)
            
        nV = (10000 + cValue - 1) % 10000
        if nV not in visited:
            queue.append((nV, cmd + 'S'))
            visited.add(nV)

        nV = cValue // 1000 + (cValue % 1000)*10
        if nV not in visited:
            queue.append((nV, cmd + 'L'))
            visited.add(nV)
        nV = cValue // 10 + (cValue % 10) * 1000
        if nV not in visited:
            queue.append((nV, cmd + 'R'))
            visited.add(nV)
    print(cmd)