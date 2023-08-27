import sys
import heapq
input = sys.stdin.readline

def getParent(a):
    if parent[a] == a:
        return a
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

def getDistance(x1,y1, x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

n = int(input())
heap = []
parent = list(range(n+1))
coordNum = dict()
cnt = 1
for i in range(n):
    x, y = map(float, input().split())
    coordNum[(x,y)] = cnt
    cnt += 1

    for nx,ny in coordNum.keys():
        cost = getDistance(x, y, nx, ny)
        heapq.heappush(heap, (cost, cnt-1, coordNum[(nx,ny)]))

result = 0
while heap:
    cost, a, b = heapq.heappop(heap)
    if not isSameParent(a, b) :
        unionParent(a, b)
        result += cost
print(round(result, 2))