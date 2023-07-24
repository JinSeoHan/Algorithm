import sys
input = sys.stdin.readline

count = 0
def DFS(start):
    global count
    visited[start] = True
    for e in edge[start]:
        if visited[e] == False:
            count += 1
            DFS(e)

n = int(input())
m = int(input())
visited = [False]*(n+1)
edge = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

DFS(1)
print(count)