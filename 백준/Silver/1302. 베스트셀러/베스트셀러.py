import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

heap = []
dic = defaultdict(int)

for i in range(int(input())):
    dic[input()] += 1

for k, v in dic.items():
    heapq.heappush(heap, (-v, k))

print(heapq.heappop(heap)[1])