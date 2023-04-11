x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print(min(x, key=x.count), min(y, key=y.count))