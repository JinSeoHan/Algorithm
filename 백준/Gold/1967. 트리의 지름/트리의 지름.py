import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
edge = [[] for i in range(n + 1)]
for i in range(n-1):
    u, v, c = map(int, input().split())
    edge[u].append((v,c))
    edge[v].append((u,c))

def DFS(cv, cc):
    global maxCost
    if cc > maxCost[1]:
        maxCost = cv, cc

    visited[cv] = True

    for nv, nc in edge[cv]:
        if not visited[nv]:
            DFS(nv, cc + nc)

visited = [False] * (n+1)
maxCost = 0, 0
DFS(1, 0)
endPoint, endCost = maxCost
visited = [False] * (n+1)
maxCost = 0, 0
DFS(endPoint, 0)
print(maxCost[1])    