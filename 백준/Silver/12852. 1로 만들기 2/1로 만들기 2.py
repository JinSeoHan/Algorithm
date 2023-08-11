import sys
from collections import deque
input = sys.stdin.readline
INF = 2*10**9

N = int(input())
visited = [False] * (N+1)

queue = deque()
queue.append((N, 0, [N]))
while queue:
    currNum, cost, currGraph = queue.popleft()

    if currNum == 1:
        break
    if visited[currNum]:
        continue

    visited[currNum] = True
    queue.append((currNum-1, cost + 1, currGraph[::] + [currNum-1]))
    if currNum % 3 == 0:
        queue.append((currNum//3, cost + 1, currGraph[::] + [currNum//3]))
    if currNum % 2 == 0:
        queue.append((currNum//2, cost + 1, currGraph[::] + [currNum//2]))

print(cost)
print(*currGraph)