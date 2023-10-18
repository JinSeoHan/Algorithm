a, b = None, None
def solution(m, n, board):
    global a ,b
    a, b = n, m
    nBoard = [[None]*m for r in range(n)]
    
    #배열 재정렬
    for c in range(n):
        for r in range(m-1, -1, -1):
            nBoard[c][-(r-m+1)] = board[r][c]
        
    flag = True
    cnt = 0
    while flag: 
        #2*2 체크
        checked = [[False]*m for r in range(n)]
        for i in range(n):
            for j in range(m):
                target = nBoard[i][j]
                checkBoard(nBoard, checked, i, j)
        #체크 삭제 및 채우기
        flag = False
        for i in range(n):
            for j in range(m-1, -1, -1):
                if checked[i][j]:
                    flag = True
                    del nBoard[i][j]
                    nBoard[i].append(None)
                    cnt += 1
    return cnt
def checkBoard(nBoard, checked, r, c):
    positions = [
        [(0,1),(1,1),(1,0)],
        [(0,1),(-1,1),(-1,0)],
        [(-1,0),(-1,-1),(0,-1)],
        [(0,-1),(1,-1),(1,0)]
    ]
    
    for position in positions:
        x1, y1 = r + position[0][0], c + position[0][1]
        x2, y2 = r + position[1][0], c + position[1][1]
        x3, y3 = r + position[2][0], c + position[2][1]
        if not validPosition(x1, y1, x2, y2, x3, y3): continue
        n1, n2, n3 = nBoard[x1][y1], nBoard[x2][y2], nBoard[x3][y3]
        if None in (n1, n2, n3): continue
        
        if nBoard[r][c] == n1 == n2 == n3:
            checked[x1][y1] = True
            checked[x2][y2] = True
            checked[x3][y3] = True
            
def validPosition(x1, y1, x2, y2, x3, y3):
    return 0 <= x1 < a and 0 <= y1 < b and 0 <= x2 < a and 0 <= y2 < b and 0 <= x3 < a and 0 <= y3 < b