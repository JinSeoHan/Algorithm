def validPosition(i, j, board):
    #row valid
    for c in range(8):
        if c == j: continue
        if board[i][c] == 'O': return False
    #column valid
    for r in range(8):
        if r == i: continue
        if board[r][j] == 'O': return False
    return True
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} ', end='')
    rookCnt = 0 #룩 개수
    #보드를 리스트에저장
    board = []
    for i in range(8):
        board.append(list(input()))
    #검사
    gameResult = True
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                rookCnt += 1
                if not validPosition(i, j, board):
                    gameResult = False
                    break
        if gameResult == False:
            break
    if gameResult and rookCnt != 8:
        gameResult = False
    print('yes') if gameResult else print('no')