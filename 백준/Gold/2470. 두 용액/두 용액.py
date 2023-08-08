import sys
input = sys.stdin.readline
INF = 2*10**10

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, N-1
minL, minR = None, None
minDiff = INF
while l < r:
    diff = arr[l] + arr[r]
    if abs(diff) < minDiff:
        minDiff = abs(diff)
        minL, minR = l, r
    if diff > 0:
        r -= 1
    else:
        l += 1
print(arr[minL], arr[minR])