import sys
input = sys.stdin.readline
INF = 10**10

def bf():
    distance[1] = 0
    for i in range(V):
        for cv, nv, c in edges:
            if distance[cv] != INF and distance[nv] > distance[cv] + c:
                distance[nv] = distance[cv] + c

                if i == V-1:
                    return False
    return True

V, E = map(int, input().split())
distance = [INF] * (V + 1)
edges = []

for e in range(E):
    u, v, c = map(int, input().split())
    edges.append((u,v,c))

if bf():
    for i in range(2, V+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)