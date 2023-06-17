import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
for i in range(1, n):
    if l[i-1] < 0 or (l[i-1] + l[i]) < 0:
        continue
    l[i] += l[i-1]
print(max(l))