import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nArr = set([input() for _ in range(n)])
mArr = [input() for _ in range(m)]

count = 0
for i in mArr:
    if i in nArr:
        count += 1
print(count)