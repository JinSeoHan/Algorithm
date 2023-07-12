import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

lo, hi = 1, k
while lo <= hi:
    mid = (lo + hi) // 2

    sum = 0
    for i in range(1, n+1):
        sum += min(mid//i, n)
    
    if sum < k:
        lo = mid + 1
    else:
        hi = mid - 1
print(hi+1)