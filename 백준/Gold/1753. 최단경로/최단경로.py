import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
first = int(input())

edges = [[] for v in range(V + 1)]
visited = [False] * (V + 1)
INF = 10**9
d = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))

def dijkstra(start):
    heap = []
    
    #start -> v까지의 최단경로
    d[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        w, v = heapq.heappop(heap)
        visited[v] = True

        for edge in edges[v]:
            ew, ev = edge
            if not visited[ev] and d[ev] > w + ew:
                d[ev] = w + ew
                heapq.heappush(heap, (d[ev], ev))

dijkstra(first)
for i in range(1, V+1):
    print('INF') if d[i] == INF else print(d[i])