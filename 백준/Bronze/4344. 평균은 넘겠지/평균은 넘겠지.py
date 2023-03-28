N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    average = sum(arr[1:]) / arr[0]
    print(f'{round(len([j for j in arr[1:] if j > average]) / arr[0] * 100, 3):.3f}%')