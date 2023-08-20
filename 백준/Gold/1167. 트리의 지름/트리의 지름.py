import sys
input = sys.stdin.readline

n = int(input())

edge = [[] for i in range(n+1)]
for i in range(n):
    info = list(map(int, input().split()))
    cv = info[0]
    idx = 1
    while info[idx] != -1:
        nv = info[idx]
        c = info[idx+1]
        edge[cv].append((c, nv))
        edge[nv].append((c, cv))
        idx += 2
        
def DFS(cv, cc):
    global result
    if cc > result[0]:
        result = (cc, cv)
    visited[cv] = True

    for nc, nv in edge[cv]:
        if not visited[nv]:
            DFS(nv, cc+nc)

result = (0, 0)
visited = [False] * (n+1)
DFS(1, 0)
endV = result[1]
result = (0, 0)
visited = [False] * (n+1)
DFS(endV, 0)
print(result[0])