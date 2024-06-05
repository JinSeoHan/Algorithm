from collections import defaultdict
import sys
input = sys.stdin.readline

mem = defaultdict(int)
n = int(input())
for _ in range(n):
    mem[input().strip()] += 1

for _ in range(n-1):
    mem[input().strip()] -= 1

for k, v in mem.items():
    if v != 0:
        print(k)