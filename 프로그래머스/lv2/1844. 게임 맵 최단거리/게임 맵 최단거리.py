from collections import deque
def solution(maps):
    BFS(maps)
    return -1 if maps[-1][-1] == 1 else maps[-1][-1] - 1

def BFS(maps):
    queue = deque()
    queue.append((0, 0))
    maps[0][0] = 2
    while queue:
        cx, cy = queue.popleft()
        for pos in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx ,ny = cx+pos[0], cy+pos[1]
            if isValid(nx, ny, len(maps), len(maps[0])) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                queue.append((nx, ny))
def isValid(x, y, ex, ey):
    return 0 <= x < ex and 0 <= y < ey