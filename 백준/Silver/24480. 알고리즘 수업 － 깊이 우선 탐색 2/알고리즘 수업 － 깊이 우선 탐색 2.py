import sys
sys.setrecursionlimit(10*200000)
input = sys.stdin.readline

count = 0
def DFS(s):
    global count
    count += 1
    visited[s] = count
    
    edge[s].sort(reverse=True)
    for e in edge[s]:
        if visited[e] == 0:
            DFS(e)

N, M, R = map(int, input().split())
visited = [0]*(N+1)

edge = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

DFS(R)
for i in range(1, N + 1):
    print(visited[i])