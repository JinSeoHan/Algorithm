import sys
from collections import deque, defaultdict
input = sys.stdin.readline

c, r = map(int, input().split())

field = [['.']*c for _ in range(r)]

# 시계방향으로 90도 돌려서 저장
for j in range(c-1, -1, -1):
    for i, v in enumerate(input().rstrip()):
        field[i][j] = v
n = int(input()) # 막대 던진 횟수
rounds = list(map(int, input().split()))

# dir값에 따라 0:왼->오 1:오->왼 순서로 미네랄 제거
def interceptMineral(field, c, dir):
    # 왼 -> 오
    if dir == 0:
        for r in range(len(field)):
            if field[r][c] == 'x':
                field[r][c] = '.'
                break
    # 오 -> 왼
    else:
        for r in range(len(field)-1, -1, -1):
            if field[r][c] == 'x':
                field[r][c] = '.'
                break
    return field

# bfs를 돌며 지상에 붙어있는 미네랄 클러스터를 표시
def bfs(i, j, visited):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = True
    while queue:
        ci, cj = queue.popleft()
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = ci+dir[0], cj+dir[1]
            if 0 <= ni < len(field) and 0 <= nj < len(field[0]) and not visited[ni][nj] and field[ni][nj] == 'x':
                visited[ni][nj] = True
                queue.append((ni, nj))

#높이를 찾음
def getHeight(i, j, visited):
    cnt = -1
    for cj in range(j, -1, -1):
        if field[i][cj] == '.': cnt += 1
        if field[i][cj] == 'x' and visited[i][cj]: break
    return cnt


# 클러스터 drop
def dropMineral(field):
    coordInfo = []
    visited = [[False]*c for _ in range(r)]

    # 떠있는 좌표를 찾음
    for i in range(r):
        bfs(i,0, visited)
    isFloat = False
    for i in range(r):
        for j in range(c):
            if field[i][j] == 'x' and not visited[i][j]:
                field[i][j] = '.'
                coordInfo.append((i,j))
                isFloat = True
    #최소 높이를 찾음
    heightResult = 1000000000
    if isFloat:
        for coord in coordInfo:
            height = getHeight(coord[0],coord[1], visited)
            heightResult = min(heightResult, height)
    #drop
    for i, j in coordInfo:
        field[i][j-heightResult] = 'x'

    return field

for i, rnd in enumerate(rounds):
    if i % 2 == 0:
        # 왼->오 요격
        field = interceptMineral(field, rnd-1, 0)
        field = dropMineral(field)
    else:
        # 오->왼 요격
        field = interceptMineral(field, rnd-1, 1)
        field = dropMineral(field)

for j in range(c):
    for i in range(r):
        print(field[i][c-j-1], end='')
    print()