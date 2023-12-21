import sys
import heapq
input = sys.stdin.readline

INF = 10**10
n = int(input())
m = int(input())

edges = [[] for i in range(n+1)]
for i in range(m):
    s, d, c = map(int, input().split())
    edges[s].append([c, d])
rs, rd = map(int, input().split())

visited = [False]*(n+1)
dist = [INF]*(n+1)
dist[rs] = 0
def dijkstra(rs, rd, edges):
    heap = []
    heapq.heappush(heap, (0, rs))

    while heap:
        cdist, cv = heapq.heappop(heap)
        if visited[cv]: continue
        visited[cv] = True

        for edge, nv in edges[cv]:
            if not visited[nv] and dist[nv] > cdist + edge:
                dist[nv] = cdist+edge
                heapq.heappush(heap, (dist[nv], nv))
    return dist[rd]
print(dijkstra(rs, rd, edges))