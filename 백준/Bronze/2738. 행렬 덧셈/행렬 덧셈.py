r, c = map(int, input().split())
m = []
for _ in range(r):
    m.append(list(map(int, input().split())))
for e in m:
    l = list(map(int, input().split()))
    for j in range(c):
        e[j] += l[j]
    print(*e)