import sys
input = sys.stdin.readline

n, c = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]
l.sort()
lo, hi = l[0], l[-1]
while lo <= hi:
    mid = (hi+lo)//2

    stack = [l[1]]
    for i in range(1, n+1):
        if l[i] - stack[-1] >= mid:
            stack.append(l[i])
    if len(stack) >= c:
        lo = mid+1
    else:
        hi = mid-1
print(hi)