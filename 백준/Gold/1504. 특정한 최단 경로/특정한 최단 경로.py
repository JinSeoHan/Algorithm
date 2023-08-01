import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
edges = [[] for r in range(N + 1)]
INF = 10**11
# 간선정보를 저장함
for e in range(E):
    u, v, c = map(int, input().split())
    edges[u].append((c, v))
    edges[v].append((c, u))
# 반드시 거쳐야하는 v1, v2
v1, v2 = map(int, input().split())

def dijkstra(start):
    result = [INF] * (N + 1)
    result[start] = 0
    heap = []
    visited = [False] * (N + 1)
    #인접노드 최단거리 갱신
    heapq.heappush(heap, (0, start))

    while heap:
        c, v = heapq.heappop(heap)
        visited[v] = True

        for ec, ev in edges[v]:
            if not visited[ev] and result[ev] > c + ec:
                result[ev] = c + ec
                heapq.heappush(heap, (c + ec, ev))
    return result

#1->v1->v2->N or 1->v2->v1->N
result = dijkstra(1)
v1Cost = result[v1]
v2Cost = result[v2]
result = dijkstra(v1)
v1v2Cost = result[v2]
v1NCost = result[N]
result = dijkstra(v2)
v2NCost = result[N]

print(-1) if INF in (v1Cost, v2Cost, v1v2Cost, v1NCost, v2NCost) else print(min(v1Cost+v1v2Cost+v2NCost, v2Cost+v1v2Cost+v1NCost))