import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def getParent(parent, f):
    if parent[f] == f: return f
    p = getParent(parent, parent[f])
    parent[f] = p
    return parent[f]

def unionParent(parent, f1, f2):
    f1 = getParent(parent, f1)
    f2 = getParent(parent, f2)
    if f1 != f2:
        parent[f2] = f1
        cnt[f1] += cnt[f2]

for _ in range(int(input())):
    parent = dict()
    cnt = dict()

    n = int(input())
    for i in range(n):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            cnt[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            cnt[f2] = 1
        unionParent(parent, f1, f2)
        print(cnt[parent[f1]])