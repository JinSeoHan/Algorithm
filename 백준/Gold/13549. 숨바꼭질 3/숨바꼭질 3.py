import sys
from collections import deque
input = sys.stdin.readline

def isValidLocation(loc):
    if 0 <= loc <= 100000:
        return True
    return False

def BFS():
    queue = deque()
    queue.append(N)
    visited[N] = 0

    while queue:
        currLoc = queue.popleft()
        if currLoc == K:
            return visited[currLoc]

        for nLoc in (currLoc*2, currLoc -1, currLoc+1):
            if isValidLocation(nLoc):
                if visited[nLoc] == -1:
                    queue.append(nLoc)
                    if nLoc == currLoc*2:
                        visited[nLoc] = visited[currLoc]
                    else:
                        visited[nLoc] = visited[currLoc] + 1


N, K = map(int, input().split())
visited = [-1] * (100001)

print(BFS())