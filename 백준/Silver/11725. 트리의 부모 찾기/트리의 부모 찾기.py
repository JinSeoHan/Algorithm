import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
parent = [0]*(n+1)

edge = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

def BFS():
    queue = deque()
    queue.append(1)

    while queue:
        cv = queue.popleft()
        visited[cv] = True

        for nv in edge[cv]:
            if not visited[nv]:
                parent[nv] = cv
                queue.append(nv)
BFS()
for i in range(2,n+1):
    print(parent[i])