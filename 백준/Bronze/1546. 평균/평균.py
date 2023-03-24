a = int(input())
arr = list(map(int, input().split()))
max = max(arr)
for i in range(a):
    arr[i] = arr[i]/max*100
print(sum(arr)/len(arr))