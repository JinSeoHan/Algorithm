import sys
input = sys.stdin.readline

n = int(input())
l1 = set(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))
for v in l2:
    print(1) if v in l1 else print(0)