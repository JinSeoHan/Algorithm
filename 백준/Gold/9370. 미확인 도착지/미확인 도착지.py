import sys
import heapq
input = sys.stdin.readline
INF = 10**10

def BFS(start):
    d = [INF] * (n + 1)
    d[start] = 0
    visited = [False] * (n + 1)

    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        c, v = heapq.heappop(heap)

        visited[v] = True

        for nc, nv in edges[v]:
            if not visited[nv] and d[nv] > c + nc:
                d[nv] = c + nc
                heapq.heappush(heap, (d[nv], nv))

    return d

for _ in range(int(input())):
    #V, E, D
    n, m, t = map(int, input().split())
    #S, V1, V2
    s, g, h = map(int, input().split())

    #edge의 정보를 저장함
    edges = [[] for v in range(n+1)]   
    for e in range(m):
        u, v, c = map(int, input().split())
        #교차로 사이의 거리 저장
        if u == g and v == h or u == h and v == g:
            middle = c
        edges[u].append((c, v))
        edges[v].append((c, u))
    #g, h 값 저장
    tList = [int(input()) for i in range(t)]


    result = BFS(s)
    
    if result[g] > result[h]:
        pos1 = h
        pos2 = g
    else:
        pos1 = g
        pos2 = h

    result2 = BFS(pos2)

    arr = []
    for t in tList:
        if result[t] == result[pos1] + middle + result2[t]:
            arr.append(t)

    arr.sort()

    print(*arr)