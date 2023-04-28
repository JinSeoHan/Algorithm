import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for i in range(n):
    num = int(input())
    arr[num] += 1

for i in range(len(arr)):
    if arr[i] == 0: continue
    for j in range(arr[i]):
        print(i)