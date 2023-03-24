N, M = map(int, input().split())
arr = [a for a in range(1, N+1)]
for n in range(M):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
print(*arr)