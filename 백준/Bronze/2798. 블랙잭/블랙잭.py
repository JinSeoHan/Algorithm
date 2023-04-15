n, m = map(int, input().split())
datas = list(map(int, input().split()))
max = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            sum = datas[i] + datas[j] + datas[k]
            if sum <= m and max < sum:
                max = sum
print(max)