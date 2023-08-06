import sys
input = sys.stdin.readline
INF = 10**10

V, E = map(int, input().split())

distance = [[INF]*(V+1) for i in range(V+1)]
for _ in range(E):
    u, v, c = map(int, input().split())
    distance[u][v] = c
    
def floydWarshall():
    for middleV in range(1, V + 1):
        for cv in range(1, V + 1):
            for nv in range(1, V + 1):
                if distance[cv][nv] > distance[cv][middleV] + distance[middleV][nv]:
                    distance[cv][nv] = distance[cv][middleV] + distance[middleV][nv]

floydWarshall()

minCycleSum = INF
for i in range(1, V + 1):
    minCycleSum = min(minCycleSum, distance[i][i])

print(-1) if minCycleSum == INF else print(minCycleSum)