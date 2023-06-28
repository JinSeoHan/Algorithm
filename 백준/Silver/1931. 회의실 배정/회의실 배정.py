import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())
for i in range(n):
    s, e = map(int, input().split())
    heapq.heappush(h, [e, s, e])
count = 0
prev = [-1, -1, -1]
while h:
    curr = heapq.heappop(h)
    if curr[1] < prev[2]:
        continue
    count += 1
    prev = curr
print(count)