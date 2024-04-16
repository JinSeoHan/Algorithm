n = int(input())
m = int(input())

board = [[0]*n for r in range(n)]
result = None

#
i, j, num = 0, 0, n**2
#중앙 1 입력
board[(n+1)//2-1][(n+1)//2-1]=1
while n > 0:
    board[i][j] = num
    if board[i][j] == m:
        result = i, j
    num -= 1
    for dir in [(1,0),(0,1),(-1,0),(0,-1)]: #하,우,상,좌
        # 4회 입력
        for t in range(n-1):
            if dir[1] == -1 and t == n-2: break
            #다음 좌표 지정
            i, j = i+dir[0], j+dir[1]
            board[i][j] = num
            if board[i][j] == m:
                result = i, j
            num -= 1
    i +=1 #한칸 아래로 이동
    n -= 2

for r in board:
    print(*r)
print(result[0]+1, result[1]+1)