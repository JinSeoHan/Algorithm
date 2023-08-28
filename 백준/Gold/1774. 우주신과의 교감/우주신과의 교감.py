import sys
import heapq
input = sys.stdin.readline

def getCost(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

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

N, M = map(int, input().split())
parent = list(range(N+1))
coordId = dict()
cnt = 1
heap = []
for i in range(N):
    x, y = map(int, input().split())
    coordId[(x,y)] = cnt
    cnt += 1

    for v in coordId.keys():
        heapq.heappush(heap, (getCost(x, y, v[0], v[1]), cnt-1, coordId[v]))

for i in range(M):
    a, b = map(int, input().split())
    unionParent(a,b)

result = 0.0
while heap:
    c, a, b = heapq.heappop(heap)
    if not isSameParent(a, b):
        unionParent(a, b)
        result += c
print(f'{round(result, 2):.2f}')