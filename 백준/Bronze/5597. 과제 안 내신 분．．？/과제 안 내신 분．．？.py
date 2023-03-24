arr = [False] * 31
for i in range(28):
    a = int(input())
    arr[a] = True
for j in range(1, 31):
    if not arr[j]: print(j)