import sys
from collections import deque
input = sys.stdin.readline

n, s, m = map(int, input().split())

v = [None] + list(map(int, input().split()))

queue = deque()
queue.append((s, 0)) #현재볼륨, 현재볼륨을 만들어낸 i, 
visited = [[False]*(m+1) for row in range(n+1)] # visited[i][j] i번째 곡일때 , 볼륨 j를만들었는지
visited[0][s] = True

result = -1
while queue:
    cv, i = queue.popleft()
    if i == n:
        result = max(result, cv)

    for case in [1, -1]:
        if i+1 < n+1:
            nv = cv+v[i+1]*case
            if 0 <= nv <= m and not visited[i+1][nv]:
                queue.append((nv, i+1))
                visited[i+1][nv] = True
print(result)