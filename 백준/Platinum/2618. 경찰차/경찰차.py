import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def calDistance(start, end):
    sx, sy = start[0], start[1]
    ex, ey = end[0], end[1]
    return abs(ex-sx) + abs(ey-sy)

def findDistance(p1, p2):
    if p1 == W or p2 == W:
        return 0
    if dp[p1][p2]:
        return dp[p1][p2]

    next = max(p1, p2) + 1
    if p1 == 0:
        dis1 = calDistance((1,1), wPositions[next])
    else:
        dis1 = calDistance(wPositions[p1], wPositions[next])

    if p2 == 0:
        dis2 = calDistance((n,n), wPositions[next])
    else:
        dis2 = calDistance(wPositions[p2], wPositions[next])

    dp[p1][p2] = min(findDistance(next, p2) + dis1, findDistance(p1, next)+ dis2)
    return dp[p1][p2]

def printOrd(p1, p2):
    if p1 == W or p2 == W:
        exit(0)

    next = max(p1, p2) + 1
    if p1 == 0:
        dis1 = calDistance((1,1), wPositions[next])
    else:
        dis1 = calDistance(wPositions[p1], wPositions[next])

    if p2 == 0:
        dis2 = calDistance((n,n), wPositions[next])
    else:
        dis2 = calDistance(wPositions[p2], wPositions[next])

    if(dp[next][p2] + dis1 < dp[p1][next] + dis2):
        print(1)
        printOrd(next, p2)
    else:
        print(2)
        printOrd(p1, next)

n = int(input())
W = int(input())
ord = []
dp = [[0]*(W+1)for r in range(W + 1)]
wPositions = [0]
for i in range(W):
    x, y = map(int, input().split())
    wPositions.append((x,y))
    
print(findDistance(0, 0))
printOrd(0,0)