import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
r = []
r.append(l[0])
for i in range(1, n):
    for j in range(len(r)):
        if l[i] == r[j]:
            break
        elif l[i] > r[j] and j == len(r) -1:
            r.append(l[i])
            break
        elif l[i] < r[j]:
            r[j] = l[i]
            break
print(len(r))