import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
r = []
r.append(l[0])
for i in range(1, n):
    if l[i] > r[-1]:
        r.append(l[i])
    else:
        for j, v in enumerate(r):
            if l[i] <= v:
                r[j] = l[i]
                break
print(len(r))