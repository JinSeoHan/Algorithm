n = int(input())
arr = set()
for i in range(n):
    arr.add(input())
arr = sorted(arr, key=lambda x:(len(x),x))
for i in arr:
    print(i)