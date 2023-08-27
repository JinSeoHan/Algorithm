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

V, E = map(int, input().split())
heap = []
result = 0
parent = list(range(V+1))

for i in range(E):
    u, v, c = map(int, input().split())
    heapq.heappush(heap, (c, u, v))

while heap:
    c, u, v = heapq.heappop(heap)

    if not isSameParent(u, v):
        unionParent(u, v)
        result += c
    
print(result)