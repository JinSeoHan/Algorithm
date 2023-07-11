import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

lo, hi = 0, max(l)+1
mid = (hi + lo) // 2
while lo < hi:
    sum = 0
    for i in l:
        if i - mid > 0:
            sum += i - mid

    if sum < m:
        hi = mid
    else:
        lo = mid + 1
    mid = (hi + lo) // 2
print(lo-1)