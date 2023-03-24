arr = []
for a in range(9):
    arr.append(int(input()))
max = max(arr)
print(max)
print(arr.index(max)+1)