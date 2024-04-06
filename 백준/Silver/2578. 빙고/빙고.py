board = []
visited = [[False]*5 for r in range(5)]

for _ in range(5):
    board.append(list(map(int, input().split())))

def checkVisited(target, board, visited):
    for i, r in enumerate(board):
        for j, v in enumerate(r):
            if v == target:
                visited[i][j] = True

def getLineCnt(visited):
    cnt = 0
    # 가로 체크
    for i in range(5):
        for j in range(5):
            if not visited[i][j]: break
            if j == 4: 
                cnt += 1
    # 세로 체크
    for j in range(5):
        for i in range(5):
            if not visited[i][j]: break
            if i == 4: 
                cnt += 1
    # 대각선 체크
    for i in range(5):
        if not visited[i][i]: break
        if i == 4: 
            cnt += 1
    for i in range(5):
        if not visited[4-i][i]: break
        if i == 4: 
            cnt += 1
    return cnt

result = None
cnt = 0
for _ in range(5):
    for v in map(int, input().split()):
        cnt += 1
        checkVisited(v, board, visited)
        if (getLineCnt(visited)) >= 3 and result == None:
            result = cnt
print(result)