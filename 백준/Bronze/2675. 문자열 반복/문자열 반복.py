s = int(input())
for _ in range(s):
    a, b = input().split()
    arr = str()
    for i in range(len(b)):
        arr += b[i] * int(a)
    print(arr)