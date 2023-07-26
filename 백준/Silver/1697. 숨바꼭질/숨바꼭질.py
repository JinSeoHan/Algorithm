import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def isValidLocation(loc):
    if 0 <= loc <= 100000:
        return True
    return False

queue = deque()
directions = [(1, -1, )]
def BFS(loc):
    if loc == k:
        print(distance[loc])
        exit(0)

    if isValidLocation(loc+1):
        if distance[loc+1] == 0:
            queue.append(loc+1)
            distance[loc+1] = distance[loc] + 1
        else:
            distance[loc+1] = min(distance[loc+1], distance[loc]+1)
    if isValidLocation(loc-1):
        if distance[loc-1] == 0:
            queue.append(loc-1)
            distance[loc-1] = distance[loc] + 1
        else:
            distance[loc-1] = min(distance[loc-1], distance[loc]+1)
    if isValidLocation(2*loc):
        if distance[2*loc] == 0:
            queue.append(2*loc)
            distance[2*loc] = distance[loc] + 1
        else:
            distance[2*loc] = min(distance[2*loc], distance[loc]+1)
    while queue:
        BFS(queue.popleft())
    
n, k = map(int, input().split())
distance = [0]*100005

BFS(n)