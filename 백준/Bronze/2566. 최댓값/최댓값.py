arr = []
mr, mc, mv = 0, 0, 0
for i in range(9):
    l = list(map(int, input().split()))
    if max(l) > mv:
        mv = max(l)
        mr = i
        mc = l.index(max(l))
print(mv)
print(mr+1, mc+1)