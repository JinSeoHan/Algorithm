import sys
input = sys.stdin.readline

def turn(board : list, n):
    newBoard = []
    for r in board:
        newBoard.append(r.copy())
    # 주 대각선 -> 중앙 열
    for i in range(n):
        newBoard[i][(n)//2] = board[i][i]
        # 중앙열 -> 부 대각선
        newBoard[i][n-i-1] = board[i][(n)//2]
        # 부 대각선 -> 중앙 행
        newBoard[(n)//2][n-i-1] = board[i][n-i-1]
        # 중앙 행 -> 주 대각선
        newBoard[i][i] = board[(n)//2][i]
    return newBoard

for _ in range(int(input())):
    n, d = map(int, input().split())
    # 2차원 배열
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    # 회전 각도 계산
    d = 360 + d if d < 0 else d
    # 각도 크기 만큼 회전
    for _ in range(d // 45):
        board = turn(board, n)
    # 출력
    for r in board:
        print(*r)