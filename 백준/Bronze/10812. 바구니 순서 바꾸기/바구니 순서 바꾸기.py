N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for i in range(M):
    s, e, m = map(int, input().split())
    arr[s-1:e] = arr[m-1:e] + arr[s-1:m-1]
print(*arr)