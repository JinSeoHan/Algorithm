import sys
sys.setrecursionlimit(10**6)
def isValid(visited, r, c):
    return 0 <= r < len(visited) and 0 <= c < len(visited[0])
def dfs(land, visited, r, c, coord):
    visited[r][c] = True
    s = 0
    
    for direction in [(0,1),(1,0),(0, -1),(-1,0)]:
        nr, nc = r+direction[0], c+direction[1]
        if isValid(visited, nr, nc) and not visited[nr][nc] and land[nr][nc] == 1:
            coord.append((nr, nc))
            s += dfs(land, visited, nr, nc, coord)
    return s + 1
def solution(land):
    answer = 0
    dic = dict()
    unique = 0
    #방문체크
    visited = [[False]*len(land[0]) for row in range(len(land))]
    for c in range(len(land[0])):
        #석유량
        for r in range(len(land)):
            #방문x + 석유발견 => dfs로 크기 찾아서 반환 + 방문체크
            if not visited[r][c] and land[r][c] == 1:
                coord = []
                coord.append((r, c))
                #s += dfs(land, visited, r, c, coord)
                s = dfs(land, visited, r, c, coord)
                #좌표정보저장
                for v in coord:
                    dic[v] = (unique,s)
                unique += 1
                
    for c in range(len(land[0])):
        temp = set()
        s = 0
        for r in range(len(land)):
            if (r, c) in dic:
                uniq, cnt = dic[(r,c)]
                if uniq not in temp:
                    temp.add(uniq)
                    s += cnt
        answer = max(answer, s)
    return answer