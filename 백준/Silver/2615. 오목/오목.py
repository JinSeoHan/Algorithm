import sys
from collections import deque
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(19)]
visited = [[[False]*4 for col in range(19)] for row in range(19)]

def valid(i, j):
    return 0 <= i < 19 and 0 <= j < 19
#가로
def dfs1(i, j, visited, target):
    visited[i][j] = True
    cnt = 0
    for dir in [(0,1),(0,-1)]:
        ni, nj = i + dir[0], j + dir[1]
        if valid(ni, nj) and not visited[ni][nj] and target == board[ni][nj]:
            cnt += dfs1(ni, nj, visited, target)
    return cnt + 1

#세로
def dfs2(i, j, visited, target):
    visited[i][j] = True
    cnt = 0
    for dir in [(1,0),(-1,0)]:
        ni, nj = i + dir[0], j + dir[1]
        if valid(ni, nj) and not visited[ni][nj] and target == board[ni][nj]:
            cnt += dfs2(ni, nj, visited, target)
    return cnt + 1
#가로위
def dfs3(i, j, visited, target):
    visited[i][j] = True
    cnt = 0
    for dir in [(-1,1),(1,-1)]:
        ni, nj = i + dir[0], j + dir[1]
        if valid(ni, nj) and not visited[ni][nj] and target == board[ni][nj]:
            cnt += dfs3(ni, nj, visited, target)
    return cnt + 1
#가로아래
def dfs4(i, j, visited, target):
    visited[i][j] = True
    cnt = 0
    for dir in [(-1,-1),(1,1)]:
        ni, nj = i + dir[0], j + dir[1]
        if valid(ni, nj) and not visited[ni][nj] and target == board[ni][nj]:
            cnt += dfs4(ni, nj, visited, target)
    return cnt + 1

def getLeftEnd(i, j, rop, cop):
    target = board[i][j]
    while valid(i, j):
        if board[i][j] != target: break
        i += rop
        j += cop
    return i-rop, j-cop
    
def gameResult(si,sj):
    ri, rj = None, None
    target = board[si][sj]

    #가로
    visited = [[False]*19 for r in range(19)]
    cnt = dfs1(si,sj, visited, target)
    if cnt == 5:
        ri, rj = getLeftEnd(si, sj, 0, -1)
    #세로
    visited = [[False]*19 for r in range(19)]
    cnt = dfs2(si,sj, visited, target)
    if cnt == 5:
        ri, rj = getLeftEnd(si, sj, -1, 0)
    #가로위
    visited = [[False]*19 for r in range(19)]
    cnt = dfs3(si,sj, visited, target)
    if cnt == 5:
        ri, rj = getLeftEnd(si, sj, 1, -1)
    #가로아래
    visited = [[False]*19 for r in range(19)]
    cnt = dfs4(si,sj, visited, target)
    if cnt == 5:
        ri, rj = getLeftEnd(si, sj, -1, -1)
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