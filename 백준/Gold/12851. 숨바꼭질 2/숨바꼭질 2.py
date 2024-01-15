from collections import deque

n, k = map(int, input().split())

fastTime = [100001]*(100001)
caseCnt = 0
queue = deque()
queue.append(n)
fastTime[n] = 0

while queue:
    cPos = queue.popleft()
    if cPos == k:
        caseCnt += 1

    for nPos in [cPos*2, cPos+1, cPos-1]:
        if 0 <= nPos < 100001 and fastTime[cPos] + 1 <= fastTime[nPos]:
            fastTime[nPos] = fastTime[cPos] + 1
            queue.append(nPos)
print(fastTime[k])
print(caseCnt)