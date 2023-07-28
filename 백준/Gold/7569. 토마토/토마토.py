import sys
from collections import deque
input = sys.stdin.readline

def isValidLocation(h,r,c):
    if 0<=h<H and 0<=r<N and 0<=c<M:
        return True
    return False

directions = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
def BFS():
    while queue:
        h, r, c = queue.popleft()
        
        for direction in directions:
            nh, nr, nc = h+direction[0], r+direction[1], c+direction[2]
            if isValidLocation(nh, nr, nc):
                if boxs[nh][nr][nc] == 0:
                    boxs[nh][nr][nc] = boxs[h][r][c] + 1
                    queue.append((nh,nr,nc))


M, N, H = map(int, input().split())
boxs = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]
queue = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxs[h][n][m] == 1:
                queue.append((h,n,m))

BFS()

result = 0
for h in range(H):
    for n in range(N):
        if 0 in boxs[h][n]:
            print(-1)
            exit(0)
        result = max(result, max(boxs[h][n]))
print(result - 1)