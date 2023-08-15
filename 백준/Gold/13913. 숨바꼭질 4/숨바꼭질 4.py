import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

time = [0] * (100001)
ord = [0] * 100001

def isValidPos(pos):
    if 0 <= pos <= 100000:
        return True
    return False

queue = deque()
queue.append(n)

while queue:
    cPos = queue.popleft()
    if cPos == k:
        break

    for nPos in cPos-1, cPos+1, cPos*2:
        if isValidPos(nPos) and time[nPos] == 0:
            time[nPos] = time[cPos] + 1
            ord[nPos] = cPos
            queue.append(nPos)

print(time[k])    
idx = k
ans = []
while True:
    ans.append(idx)
    if idx == n:
        break
    idx = ord[idx]

print(*ans[::-1])