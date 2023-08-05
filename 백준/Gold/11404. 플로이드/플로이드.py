import sys
input = sys.stdin.readline
INF = 10**10

V = int(input())
E = int(input())

distance = [[INF]*(V+1) for i in range(V+1)]
for e in range(E):
    u, v, c = map(int, input().split())
    if distance[u][v] > c:
        distance[u][v] = c

def floydWarshall():

    for middleV in range(1, V+1):
        distance[middleV][middleV] = 0
        for cv in range(1, V+1):
            for nv in range(1, V+1):
                if distance[cv][nv] > distance[cv][middleV] + distance[middleV][nv]:
                    distance[cv][nv] = distance[cv][middleV] + distance[middleV][nv]
                    
floydWarshall()

for i in range(1, V + 1):
    for j in range(1, V + 1):
        print(0, end=' ') if distance[i][j] == INF else print(distance[i][j], end=' ')
    print()