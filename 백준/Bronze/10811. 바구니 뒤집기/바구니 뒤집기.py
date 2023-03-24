a, b = map(int, input().split())
arr = [i for i in range(1,a+1)]
for i in range(b):
    c, d = map(int, input().split())
    for j in range((d-c)//2+1):
        arr[c+j-1], arr[d-j-1] = arr[d-j-1], arr[c+j-1]
print(*arr)