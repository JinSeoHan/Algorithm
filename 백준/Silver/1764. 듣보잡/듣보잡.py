import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nSet = set()
mSet = set()

for i in range(n):
    nSet.add(input().strip('\n'))
for i in range(m):
    mSet.add(input().strip('\n'))
result = list(nSet & mSet)
result.sort()
print(len(result))
for i in result:
    print(i)