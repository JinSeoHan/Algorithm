import sys
input = sys.stdin.readline
INF = 10**9

n = int(input())
m = int(input())
dist = [[INF]*(n + 1) for r in range(n + 1)]

ord = [[[0] for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    u, v, c = map(int, input().split())
    if dist[u][v] > c:
        dist[u][v] = c
        ord[u][v] = [u, v]

for midV in range(1, n + 1):
    dist[midV][midV] = 0
    ord[midV][midV] = [0]
    for s in range(1, n + 1):
        for d in range(1, n + 1):
            if dist[s][d] > dist[s][midV] + dist[midV][d]:
                dist[s][d] = dist[s][midV] + dist[midV][d]
                ord[s][d] = ord[s][midV] + ord[midV][d][1:]
for i in range(1, n+1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
    print()
for i in range(1,n+1):
    for j in range(1, n+1):
        if ord[i][j][0] != 0:
            print(len(ord[i][j]), end=' ')
        print(*ord[i][j])
