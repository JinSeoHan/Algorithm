direction = [(0,1),(1,0),(0,-1),(-1,0)]#R,D,L,U 시계방향으로 저장
n, m = None, None
#방향 회전
def turn(d, strDir):
    if strDir == 'R':
        return (d + 1)%4
    elif strDir == 'L':
        return (d - 1)%4
    else:
        return d
#다음 노드로 이동
def move(r, c, d):
    return (r+direction[d][0])%n, (c+direction[d][1])%m
def solution(grid):
    global n, m
    n, m = len(grid), len(grid[0])
    answer = []
    visited = [[[False]*4 for col in range(m)] for row in range(n)] 
    
    for r in range(n):
        for c in range(m):
            for d in range(4):
                cnt = 0
                cr, cc, cd = r, c, d
                while not visited[cr][cc][cd]:
                    visited[cr][cc][cd] = True
                    cnt += 1
                    cr, cc = move(cr, cc, cd)
                    cd = turn(cd, grid[cr][cc])
                if cnt : answer.append(cnt)
                    
    
    return sorted(answer)