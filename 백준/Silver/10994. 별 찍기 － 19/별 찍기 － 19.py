import sys
input = sys.stdin.readline

num = int(input())
board = []
board = [['*']*((num-1)*4+1) for row in range((num-1)*4+1)]

def pt(n, si,sj):
    global board
    if n == 1: return
    # 가로1 삭제
    for j in range(sj+1,sj+(n-1)*4+1-1):
        board[si+1][j] = ' '
    # 가로2 삭제
    for j in range(sj+1,sj+(n-1)*4+1-1):
        board[si+((n-1)*4+1-2)][j] = ' '
    # 세로1삭제
    for i in range(si+2, si+(n-1)*4+1-2):
        board[i][sj+1] = ' '
    # 세로2삭제
    for i in range(si+2, si+(n-1)*4+1-2):
        board[i][sj+ (n-1)*4+1-2] = ' '
    pt(n-1, si+2, sj+2)
pt(num, 0, 0)
for r in board:
    for c in r:
        print(c, end='')
    print()