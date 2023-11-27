def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1]) + 1
    result = 0
    for row in board:
        m = max(row)
        result = max(result, m)
    return result*result