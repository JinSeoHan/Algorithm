from math import ceil
n, a, b = map(int, input().split())
cnt = 0
while a != b:
    cnt += 1
    a, b = ceil(a/2), ceil(b/2)
print(cnt)