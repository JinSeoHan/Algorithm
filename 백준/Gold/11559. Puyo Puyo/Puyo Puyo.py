import sys, copy

input = sys.stdin.readline

field = [['.']*12 for r in range(6)]

for j in range(12):
    r = input().rstrip()
    for i in range(6):
        field[i][11-j] = r[i]

cnt = 0
def dfs(i, j, v, visited, board):
    global cnt
    cnt += 1
    board[i][j] = '*'
    visited[i][j] = True
    for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
        ni, nj = i+dir[0], j+dir[1]
        if 0 <= ni < 6 and 0 <= nj < 12 and not visited[ni][nj] and board[ni][nj] == v:
            dfs(ni,nj,v,visited, board)

result = 0
def puyopuyo():
    global cnt, field, result
    flag = True
    while flag:
        flag = False
        visited = [[False]*12 for r in range(6)]
        for i in range(6):
            for j in range(12):
                if field[i][j] == '.': break
                if visited[i][j]: continue

                cnt = 0
                field2 = copy.deepcopy(field)

                dfs(i, j, field[i][j], visited, field2)
                if cnt >= 4:
                    field = field2
        # '*'지우기
        for i in range(6):
            for j in range(12):
                while field[i][j] == '*':
                    del field[i][j]
                    field[i].append('.')
                    flag = True
        if flag:
            result += 1

puyopuyo()
print(result)