n = int(input())
arr = set()
for i in range(n):
    arr.add(int(input()))
arr = sorted(arr)
[print(i) for i in arr]