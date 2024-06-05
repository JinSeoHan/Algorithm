import sys

input = sys.stdin.readline

for _ in range(int(input())):
    mem = set()
    input()
    for v1 in list(map(int, input().split())):
        mem.add(v1)
    
    input()
    for v2 in list(map(int, input().split())):
        print(1) if v2 in mem else print(0)
