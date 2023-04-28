arr = list()
for i in range(5):
    arr.append(int(input()))
arr = sorted(arr)
print(sum(arr)//5)
print(arr[2])