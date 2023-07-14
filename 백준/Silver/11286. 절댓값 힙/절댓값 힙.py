import sys
from heapq import heappop, heappush
input = sys.stdin.readline

h = []
for _ in range(int(input())):
    if (v := int(input())) == 0:
        if not h:
            print(0)
        else:
            print(heappop(h)[1])
    else:
        heappush(h, (abs(v), v))