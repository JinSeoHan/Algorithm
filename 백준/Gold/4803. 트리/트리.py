import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def DFS(s, parent):
    visited[s] = True
    result = True

    for i in edge[s]:
        if not visited[i]:
            vertexs.remove(i)
            if DFS(i, s) == False:
                return False
        elif i != parent:
            return False
    return result

case = 0
while True:
    n, m = map(int , input().split())
    if n == 0 and m == 0:
        break
    edge = [[] for i in range(n+1)]
    vertexs = set(range(1,n+1))
    visited = [False] * (n+1)
    for i in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    
    cnt = 0
    while vertexs:
        if DFS(vertexs.pop(), 0):
            cnt += 1
    
    case += 1
    print(f'Case {case}: ',end='')
    if cnt == 0:
        print('No trees.')
    elif cnt == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {cnt} trees.')