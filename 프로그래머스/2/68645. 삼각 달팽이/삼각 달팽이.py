cnt = 0
len = None
def valid(x,y):
    return 0 <= x < len and 0 <= y < len
def step1(board, sx, sy, n):
    global cnt
    for i in range(n):
        if valid(sx+i, sy) and board[sx+i][sy] == 0:
            cnt += 1
            board[sx+i][sy] = cnt
        
def step2(board, sx, sy, n):
    global cnt
    sx, sy = sx+n-1, sy + 1
    for i in range(n-1):
        if valid(sx, sy+i) and board[sx][sy+i] == 0:
            cnt += 1
            board[sx][sy+i] = cnt
        
def step3(board, sx, sy, n):
    global cnt
    sx, sy = sx+n-2, sy+n-2
    for i in range(n-2):
        if valid(sx-i, sy-i) and board[sx-i][sy-i] == 0:
            cnt += 1
            board[sx-i][sy-i] = cnt
def solution(n):
    global cnt, len
    len = n
    board = [[0]*n for i in range(n)]
    
    sx, sy  = 0,0 
    while board[sx][sy] == 0:
        step1(board, sx, sy, n)
        step2(board, sx, sy, n)
        step3(board, sx, sy, n)
        
        n -= 3
        if n < 1:
            break
        sx, sy = sx + 2, sy + 1
    result = []
    
    for i in range(len):
        for j in range(len):
            if board[i][j] == 0:
                break
            result.append(board[i][j])
            
    
    return result