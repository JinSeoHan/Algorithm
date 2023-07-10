import sys
input = sys.stdin.readline

k, n = map(int, input().split())

l = [int(input()) for _ in range(k)]
lo, hi = 0, max(l)+1
mid = (hi+lo)//2
result = 0
while lo!=hi:
    count = 0
    for i in l:
        count += i//mid

    if count >= n:
        lo = mid + 1
    else:
        hi = mid
    mid = (hi+lo)//2

print(lo-1)
        