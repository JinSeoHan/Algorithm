from collections import deque
def isValid(x, y,maps):
    return 0 <= x < len(maps) and 0 <= y < len(maps[0])
def solution(maps):
    x,y = None, None
    queue = deque()
    #시작 위치를 찾음
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x, y = i, j
    # S -> L 최단거리찾기
    queue.append((x, y, 0))
    visited = [[0]*len(maps[0]) for row in range(len(maps))]
    lx, ly, lcost= None, None, None
    while queue:
        cx, cy, ccost = queue.popleft()
        if maps[cx][cy] == 'L':
            lx, ly, lcost  = cx, cy, ccost
            break
        
        for di in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cx + di[0], cy + di[1]
            if isValid(nx, ny,maps) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx,ny,ccost+1))
    if lcost == None:return -1
    #L->E 최단거리
    queue = deque()
    queue.append((lx, ly, lcost))
    visited = [[0]*len(maps[0]) for row in range(len(maps))]
    visited[lx][ly] = lcost
    ex, ey, ecost= None, None, None
    while queue:
        cx, cy, ccost = queue.popleft()
        
        if maps[cx][cy] == 'E':
            return ccost
        for di in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cx + di[0], cy + di[1]
            if isValid(nx, ny,maps) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx,ny,ccost+1))
    return -1
    


            
