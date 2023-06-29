import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int, input().split()))
l.sort()
for _ in range(2):
    for i in range(1, n + 1):
        l[i] += l[i-1]
print(l[-1])