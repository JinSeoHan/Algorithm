from collections import deque
def isValid(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])
def getStart(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return i, j
def getDesCoord(board, dir, x, y):
    nx, ny = x, y
    while isValid(board, nx, ny) and board[nx][ny] != 'D':
        nx, ny = nx + dir[0], ny + dir[1]
    return nx-dir[0], ny-dir[1] 
        
def solution(board):
    
    queue = deque()
    sx, sy = getStart(board)
    visited = [[False]*len(board[0]) for row in range(len(board))]
    visited[sx][sy] = True
    queue.append((sx, sy, 0, visited))
    
    while queue:
        cx, cy, ccnt, cvisited = queue.popleft()
        if board[cx][cy] == 'G':
            return ccnt
        
        for dir in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            nx, ny = getDesCoord(board, dir, cx, cy)
            
            if (cx,cy) != (nx, ny) and not visited[nx][ny]:
                nvisited = cvisited.copy()
                nvisited[nx][ny] = True
                queue.append((nx, ny, ccnt+1, nvisited))
                
    return -1