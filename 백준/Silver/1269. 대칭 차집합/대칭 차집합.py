import sys
input = sys.stdin.readline
aN, bN = map(int, input().split())
aSet = set(map(int, input().split()))
aSet.update(map(int, input().split()))
c = len(aSet)
print((c-aN) + (c-bN))