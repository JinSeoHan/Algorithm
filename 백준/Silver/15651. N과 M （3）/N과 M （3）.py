import sys
input = sys.stdin.readline

def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return

    for i in range(1, n + 1):
        l.append(i)
        dfs()
        l.pop()

n, m = map(int, input().split())
l = []

dfs()
