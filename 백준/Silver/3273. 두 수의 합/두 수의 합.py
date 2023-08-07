import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
l, r = 0, n-1

arr.sort()
cnt = 0
while l < r:
    sum = arr[l] + arr[r]
    if sum == x:
        cnt += 1
        l += 1
    elif sum > x:
        r -= 1
    elif sum < x:
        l += 1

print(cnt)