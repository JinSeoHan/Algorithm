import sys
input = sys.stdin.readline

def DFS(s):
    global cnt
    cnt += 1
    visited[s] = True
    vSet.remove(s)
    if len(vSet) == 0:
        return

    for e in edge[s]:
        if not visited[e]:
            DFS(e)

for _ in range(int(input())):
    n, m = map(int ,input().split())

    edge = [[] for i in range(n+1)]
    vSet = set(range(1, n+1))
    visited = [False] * (n+1)
    for i in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    cnt = 0
    DFS(edge[-1][-1])
    print(cnt-1)