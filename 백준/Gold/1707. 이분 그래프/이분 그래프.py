import sys
from collections import deque
input = sys.stdin.readline

def BFS(startV):
    queue = deque()
    queue.append(startV)
    visited[startV] = 1
    
    while queue:
        currV = queue.pop()
        
        if currV in unUsedVertexes:
            unUsedVertexes.remove(currV)

        for nV in edges[currV]:
            if visited[nV] == 0:
                queue.append(nV)
                visited[nV] = -visited[currV]
            elif visited[nV] == visited[currV]:
                return False
    return True

unUsedVertexes = None
for _ in range(int(input())):
    V, E = map(int, input().split())
    
    unUsedVertexes = {i for i in range(1, V+1)}
    edges = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for __ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    isBipartite = True
    while unUsedVertexes:
        isBipartite = BFS(unUsedVertexes.pop())
        
        if not isBipartite:
            break
    print('YES') if isBipartite else print('NO')