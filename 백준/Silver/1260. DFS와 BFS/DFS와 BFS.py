import sys
sys.setrecursionlimit(10**5)
from collections import deque
input = sys.stdin.readline

def DFS(start):
    visited1[start] = True
    result1.append(start)
    
    edge[start].sort()
    for e in edge[start]:
        if visited1[e] == False:
            DFS(e)

queue = deque()
def BFS(start):
    result2.append(start)
    for e in edge[start]:
        if visited2[e] == False:
            visited2[e] = True
            queue.append(e)
    if queue:
        BFS(queue.popleft())

N, M, V = map(int, input().split())
edge = [[] for i in range(N + 1)]
visited1 = [False]*(N + 1)
visited2 = [False]*(N + 1)
result1 = []
result2 = []

for _ in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

DFS(V)
visited2[V] = True
BFS(V)
print(*result1)
print(*result2)