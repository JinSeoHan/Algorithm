from collections import deque

def bfs(s):
    queue = deque()
    queue.append((1,0,0)) # 이모티콘 수, 소요시간, 클립보드
    visited = [[False]*1001 for row in range(1001)]
    visited[1][0] = True
    while queue:
        cEmoCnt, cTime, cClip =  queue.popleft()

        if cEmoCnt == s:
            return cTime

        # case1
        if not visited[cEmoCnt][cEmoCnt]:
            visited[cEmoCnt][cEmoCnt] = True
            queue.append((cEmoCnt, cTime+1, cEmoCnt))
        # case2
        if 0 <= cEmoCnt+cClip < 1001 and not visited[cEmoCnt+cClip][cClip]:
            visited[cEmoCnt+cClip][cClip] = True
            queue.append((cEmoCnt+cClip, cTime+1, cClip))
        # case3
        if cEmoCnt > 0 and not visited[cEmoCnt-1][cClip]:
            visited[cEmoCnt-1][cClip] = True
            queue.append((cEmoCnt-1, cTime+1, cClip))

print(bfs(int(input())))