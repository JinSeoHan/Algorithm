import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(19)]

#범위 체크
def valid(i, j):
    return 0 <= i < 19 and 0 <= j < 19
# directions방향의 돌 개수를 찾음
def dfs(i, j, visited, target, directions):
    visited[i][j] = True
    cnt = 0
    for dir in directions:
        ni, nj = i + dir[0], j + dir[1]
        if valid(ni, nj) and not visited[ni][nj] and target == board[ni][nj]:
            cnt += dfs(ni, nj, visited, target, directions)
    return cnt + 1
# 시작점을 찾음
def getLeftEnd(i, j, rop, cop):
    target = board[i][j]
    while valid(i, j):
        if board[i][j] != target: break
        i += rop
        j += cop
    return i-rop, j-cop
#이동방향 정보 : 가로,세로,가로위,가로아래
directionsInfo = [[(0,1),(0,-1)],[(1,0),(-1,0)],[(-1,1),(1,-1)],[(1,1),(-1,-1)]]
def gameResult(si,sj):
    ri, rj = None, None
    target = board[si][sj]

    # 이동방향으로 이동
    for dirInfo in directionsInfo:
        visited = [[False]*19 for r in range(19)]
        cnt = dfs(si,sj,visited,target, dirInfo)
        if cnt == 5:
            rop, cop = dirInfo[1][0], dirInfo[1][1]
            ri, rj = getLeftEnd(si, sj, rop, cop)
    return ri, rj

for i in range(19):
    for j in range(19):
        if board[i][j] == 0: continue
        ri, rj = gameResult(i,j)
        if (ri, rj) != (None, None):
            print(board[i][j])
            print(ri+1, rj+1)
            exit()
print(0)