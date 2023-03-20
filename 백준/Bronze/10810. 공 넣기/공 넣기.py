arrLength, loop = map(int, input().split())
arr = [0] * arrLength
for i in range(loop):
    a, b, c = map(int, input().split())
    for j in range(a-1, b):
        arr[j] = c
for i in range(arrLength):
    print(arr[i], end=' ')