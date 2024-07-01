from math import ceil
n, m = map(int, input().split())

packCost = 10000
unitCost = 10000
for _ in range(int(m)):
    a, b = map(int, input().split())

    packCost = min(packCost, a)
    unitCost = min(unitCost, b)

# 전체를 패키지로 구입한 경우
nCnt  = n
v1 = ceil(nCnt/6)*packCost
# 패키지 개수 + 낱개로 구입한 경우
nCnt  = n
v2 = (nCnt//6)*packCost + (nCnt%6)*unitCost
# 전체 낱개로 구입한 경우
v3 = unitCost*n

print(min(v1,v2,v3))