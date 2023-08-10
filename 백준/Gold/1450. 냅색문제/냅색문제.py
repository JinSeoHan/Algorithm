import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

lArr, rArr = arr[:N//2], arr[N//2:]

lsumComb, rsumComb = [], []
for i in range(len(lArr) + 1):
    for com in combinations(lArr, i):
        lsumComb.append(sum(com))
for i in range(len(rArr)+1):
    for com in combinations(rArr, i):
        rsumComb.append(sum(com))

lsumComb.sort()
cnt = 0
for rcombNum in rsumComb:
    
    l, r = 0, len(lsumComb)-1
    while l <= r:
        mid = (l+r)//2
        if lsumComb[mid] + rcombNum > C:
            r = mid -1
        else:
            l = mid + 1
    cnt += r + 1

print(cnt)