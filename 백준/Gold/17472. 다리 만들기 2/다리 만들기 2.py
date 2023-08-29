import sys
import heapq
from collections import deque
input = sys.stdin.readline

def getParent(a):
    if parent[a] == a: return a
    parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isSameParent(a, b):
    return getParent(a) == getParent(b)
    

def isValid(x, y):
    return 0 <= x < n and 0 <= y < m

def BFS(x, y, id):
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        matrix[cx][cy] = id
        for position in (0,1),(1,0),(0,-1),(-1,0):
            nx, ny = cx+position[0], cy+position[1]
            if isValid(nx, ny) and matrix[nx][ny] == 1:
                queue.append((nx,ny))

n, m = map(int, input().split())

matrix = []
for r in range(n):
    r = list(map(int, input().split()))
    matrix.append(r)

# 섬에 id부여
cnt = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt += 1
            BFS(i, j, cnt)
#섬사이 최단거리
heap = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 0:
            islandId = matrix[i][j]
            #l, r, u, d
            for code in range(1,5):
                distance = 0
                if code == 1:
                    r, c = i, j-1
                    while isValid(r, c):
                        distance += 1
                        if matrix[r][c] != matrix[i][j]:
                            if matrix[r][c] and matrix[r][c] != islandId and distance > 2:
                                heapq.heappush(heap, (distance-1, islandId, matrix[r][c]))
                            break
                        c -= 1
                if code == 2:
                    r, c = i, j+1
                    while isValid(r, c):
                        distance += 1
                        if matrix[r][c] != 0:
                            if matrix[r][c] != islandId and distance > 2:
                                heapq.heappush(heap, (distance-1, islandId, matrix[r][c]))
                            break
                        c += 1
                if code == 3:
                    r, c = i-1, j
                    while isValid(r, c):
                        distance += 1
                        if matrix[r][c] != 0:
                            if matrix[r][c] != islandId and distance > 2:
                                heapq.heappush(heap, (distance-1, islandId, matrix[r][c]))
                            break
                        r -= 1
                if code == 4:
                    r, c = i+1, j
                    while isValid(r, c):
                        distance += 1
                        if matrix[r][c] != 0:
                            if matrix[r][c] != islandId and distance > 2:
                                heapq.heappush(heap, (distance-1, islandId, matrix[r][c]))
                            break
                        r += 1

result = 0
parent = list(range(cnt+1))
edgeCnt = 0
while heap:
    d, a, b = heapq.heappop(heap)
    if not isSameParent(a, b):
        edgeCnt += 1
        unionParent(a, b)
        result += d
print(result) if edgeCnt == cnt-2 else print(-1)