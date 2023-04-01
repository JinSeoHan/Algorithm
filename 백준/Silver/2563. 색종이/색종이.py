arr = [[0]*101 for _ in range(101)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
result = 0
for i in arr:
    result += sum(i)
print(result)