def solution(board):
    #0또는 x를 잘못 놓은 경우
    oCnt, xCnt = 0, 0
    for i in board:
        oCnt += i.count('O')
        xCnt += i.count('X')
    temp = oCnt - xCnt
    if temp not in [0, 1]:
        return 0
    
    cols = list(zip(*board))
    oCnt , xCnt = 0, 0
    for i in range(3):
        if cols[i].count('O') == 3 or board[i].count('O') == 3:
            oCnt += 1
        elif cols[i].count('X') == 3 or board[i].count('X') == 3:
            xCnt += 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        oCnt += 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        xCnt += 1
    if board[2][0] == board[1][1] == board[0][2] == 'O':
        oCnt += 1
    if board[2][0] == board[1][1] == board[0][2] == 'X':
        xCnt += 1

    if oCnt and xCnt: return 0
    if oCnt == 1 and temp != 1: return 0
    if xCnt == 1 and temp != 0: return 0
    return 1