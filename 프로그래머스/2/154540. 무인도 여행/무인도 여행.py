import sys
sys.setrecursionlimit(10**5)
def isValid(i, j, maps):
    return 0 <= i < len(maps) and 0 <= j < len(maps[0])
def dfs(i, j, maps, visited):
    cnt = 0
    visited[i][j] = True
    for position in [(0,1),(1,0),(0,-1),(-1,0)]:
        ni,nj = i + position[0], j + position[1]
        
        if not isValid(ni,nj, maps) or visited[ni][nj] or maps[ni][nj] == 'X': continue
        cnt += int(dfs(ni,nj,maps, visited))
    return cnt + int(maps[i][j])
        
def solution(maps):
    result = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i, row in enumerate(maps):
        for j, v in enumerate(row):
            if visited[i][j] or v == 'X': 
                continue
            result.append(dfs(i, j, maps, visited))
    
    return [-1] if len(result) == 0 else sorted(result)