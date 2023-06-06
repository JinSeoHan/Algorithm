import sys
input = sys.stdin.readline

def dfs(startNum):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return 
    
    for i in range(startNum, n + 1):
        l.append(i)
        dfs(i)
        l.pop()

n, m = map(int, input().split())
l = []
dfs(1)
