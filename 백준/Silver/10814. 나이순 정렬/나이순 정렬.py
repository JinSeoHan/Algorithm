import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = input().split()
    arr.append((int(a), b))

arr.sort(key=lambda x : x[0])
for i in arr:
    print(*i)