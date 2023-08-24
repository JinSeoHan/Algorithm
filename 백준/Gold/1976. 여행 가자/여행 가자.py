import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
m = int(input())
edge = [[] for i in range(n+1)]
for i in range(1, n+1):
    info = list(map(int ,input().split()))
    for j, v in enumerate(info, 1):
        if info[j-1] == 1:
            edge[i].append(j)
root = list(map(int, input().split()))

visited = [False] * (n+1)
result = set()
def DFS(s):
    result.add(s)
    visited[s] = True
    for e in edge[s]:
        if not visited[e]:
            DFS(e)
DFS(root[0])
for i in root:
    if i not in result:
        print("NO")
        exit(0)
print("YES")