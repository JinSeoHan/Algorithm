import sys
input = sys.stdin.readline
INF = 10**6

N, S = map(int, input().split())
arr = list(map(int, input().split()))

l, r = -1, -1
cnt = 0
sum = 0
minCnt = INF
while r < N:
    if sum < S:
        r += 1
        cnt += 1
        if r < N:
            sum += arr[r]
    else:
        l += 1
        cnt -= 1
        sum -= arr[l]
    if sum >= S:
        minCnt = min(minCnt, cnt)

print(0) if minCnt == INF else print(minCnt)