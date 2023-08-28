import sys
import heapq
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

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    parent = list(range(M+1))
    heap = []
    totalCost = 0

    for i in range(N):
        u, v, c = map(int, input().split())
        totalCost += c
        heapq.heappush(heap, (c, u, v))

    mstCost = 0
    while heap:
        cost, a, b = heapq.heappop(heap)

        if not isSameParent(a, b):
            unionParent(a, b)
            mstCost += cost

    print(totalCost-mstCost)