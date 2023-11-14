from collections import deque

def isValid(i, j):
    return 0 <= i <5 and 0 <= j < 5

def bfs(i, j, place):
    visited = [[0] * 5 for row in range(5)]       
    visited[i][j] = 1
    queue = deque()
    queue.append((i, j))
    
    while queue:
        ci, cj = queue.popleft()
        
        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = ci+direction[0], cj+direction[1]
            if not isValid(ni, nj) or visited[ni][nj] != 0 or place[ni][nj] == 'X':
                continue
                
                
            visited[ni][nj] = visited[ci][cj] + 1
            if place[ni][nj] == 'P':
                if visited[ni][nj] <= 3:
                    return False
                continue
            queue.append((ni,nj))
            
    return True
    
            
def solution(places):
    result = []
    for place in places:
        flag = True
        for i, row in enumerate(place):
            for j, v in enumerate(row):
                if v != 'P':
                    continue
                if not bfs(i, j, place):
                    flag = False
                    result.append(0)
                    break
            if not flag: break
        if flag:
            result.append(1)
    return result