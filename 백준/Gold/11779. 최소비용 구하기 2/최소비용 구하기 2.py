import sys
import heapq
INF = 10**9
input = sys.stdin.readline

n = int(input())
m = int(input())
edge = [[] for i in range(n+1)]
mem = [INF] * (n+1)
for i in range(m):
    u, v, c = map(int, input().split())
    edge[u].append((c, v))
s, d = map(int, input().split())

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, s, [s]))
    
    while True:
        cc, cv, ord = heapq.heappop(heap)
        if cv == d:
            return ord
        for nc, nv in edge[cv]:
            if mem[nv] > cc + nc:
                mem[nv] = cc + nc
                heapq.heappush(heap, (mem[nv], nv,ord + [nv]))
ans = dijkstra()
print(mem[d])
print(len(ans))
print(*ans)