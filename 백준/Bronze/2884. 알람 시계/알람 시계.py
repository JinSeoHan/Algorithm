h, m = map(int, input().split())
a = m-45
if a < 0:
    if h == 0:
        h = 24
    print(h-1, 60+a)
else:
    print(h, a)