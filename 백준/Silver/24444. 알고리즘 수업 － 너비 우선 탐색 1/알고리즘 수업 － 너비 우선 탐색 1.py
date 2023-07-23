import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)

count = 1
def BFS(s):
    global count
    edge[s].sort()
    for e in edge[s]:
        if visited[e] == 0:
            queue.append(e)
            count += 1
            visited[e] = count
    if queue:
        BFS(queue.popleft())

N, M, R = map(int, input().split())
edge = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
queue = deque()

for _ in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

visited[R] = count
BFS(R)
for i in range(1, N+1):
    print(visited[i])