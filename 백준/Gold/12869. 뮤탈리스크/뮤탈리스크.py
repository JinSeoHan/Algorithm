import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

n = int(input())

l = [0, 0, 0, 0]
temp = list(map(int, input().split()))

for i, v in enumerate(temp):
    l[i] = temp[i]


def minusToZero(n1, n2, n3):
    if n1 < 0:
        n1 = 0
    if n2 < 0:
        n2 = 0
    if n3 < 0:
        n3 = 0
    return n1, n2, n3

def bfs(l):
    visited = [[[False]*61 for j in range(61)] for i in range(61)]
    queue = deque()
    queue.append(l)
    while queue:
        c1, c2, c3, cnt = queue.popleft()

        for attackV in permutations((9, 3, 1), 3):
            n1, n2, n3 = c1-attackV[0], c2-attackV[1], c3-attackV[2]
            n1, n2, n3 = minusToZero(n1, n2, n3)
            if n1 == 0 and n2 == 0 and n3 == 0:
                return cnt + 1
            if not visited[n1][n2][n3]:
                queue.append([n1,n2,n3,cnt+1])
                visited[n1][n2][n3] = True
print(bfs(l))