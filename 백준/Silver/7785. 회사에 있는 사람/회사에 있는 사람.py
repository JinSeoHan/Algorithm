import sys
input = sys.stdin.readline

n = int(input())

rSet = set()
for i in range(n):
    name, result = input().split()
    if (result == 'enter'):
        rSet.add(name)
    else:
        rSet.remove(name)
rSet = sorted(rSet, reverse=True)
for i in rSet:
    print(i)