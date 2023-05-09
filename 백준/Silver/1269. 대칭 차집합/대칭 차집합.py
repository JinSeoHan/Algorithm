import sys
input = sys.stdin.readline

aN, bN = map(int, input().split())
aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))
print(len((aSet-bSet) | (bSet-aSet)))