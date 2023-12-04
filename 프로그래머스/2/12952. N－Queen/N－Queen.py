cnt = 0
def solution(n):
    
    check = [[0]*n for row in range(n)]
    
    visited = [0]*n
    dfs(n, visited, 0)
    return cnt
            
def isValid(visited, depth, i):
    for v in visited:
        if v != 0:
            x, y = v
            if y == i or y-x == i-depth or x+y == depth+i:
                return False
    return True
def dfs(n, visited, depth):
    global cnt
    if depth == n:
        cnt += 1
    
    for i in range(n):
        if visited[i]: continue
        if isValid(visited, depth, i):
            visited[i] = (depth, i)
            dfs(n, visited, depth+1)
            visited[i] = 0
            