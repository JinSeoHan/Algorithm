import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


graph = [[] for v in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topologySort():
    queue = deque()
    result = []
    for v in range(1, n+1):
        if indegree[v] == 0:
            queue.append(v)
    
    for i in range(1, n+1):
        cv = queue.popleft()
        result.append(cv)

        for nv in graph[cv]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                queue.append(nv)
    return result
print(*topologySort())