import sys
from heapq import heappop, heappush
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    if (v := int(input())) == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, v)