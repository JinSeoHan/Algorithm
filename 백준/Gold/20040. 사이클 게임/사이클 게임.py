import sys
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

def findUnion(a, b):
    return getParent(a) == getParent(b)

n, m = map(int, input().split())
parent = list(range(n+1))
cnt = 0
result = 0
flag = True
for i in range(m):
    u, v = map(int, input().split())
    cnt += 1

    if flag and findUnion(u, v):
        result = cnt
        flag = False
    if flag:
        unionParent(u, v)
print(result)    