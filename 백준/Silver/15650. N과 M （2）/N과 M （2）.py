def dfs(startNum):
    if startNum > n+1:
       return
    if len(s) == m:
       print(' '.join(map(str, s)))
       return

    for i in range(startNum, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()
        
n, m = map(int, input().split())
s = []
visited = [False] * (n+1)
dfs(startNum=1)