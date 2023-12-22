import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
heap = []
for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

def getParent(parent, a):
    if parent[a] == a: return a
    parent[a] = getParent(parent, parent[a])
    return parent[a]
def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
def isCycle(parent, a, b):
    return getParent(parent, a) == getParent(parent, b)


parent = [i for i in range(v+1)]
result = 0
for i in range(v-1):
    c, a, b = heapq.heappop(heap)
    while isCycle(parent, a, b):
        c, a, b = heapq.heappop(heap)
    union(parent, a, b)
    result += c
print(result)