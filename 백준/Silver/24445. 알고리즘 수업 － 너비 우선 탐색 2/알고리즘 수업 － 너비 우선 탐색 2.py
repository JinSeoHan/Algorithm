import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

count = 1
def BFS(start):
    global count
    
    if edge[start]:
        edge[start].sort(reverse=True)

    for e in edge[start]:
        if visited[e] == 0:
            count += 1
            visited[e] = count
            queue.append(e)
    if queue:
        BFS(queue.popleft())

N, M, R = map(int, input().split())
edge = [[] for i in range(N+1)]
visited = [0]*(N+1)
queue = deque()
for _ in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

visited[R] = count
BFS(R)
for i in range(1, N+1):
    print(visited[i])