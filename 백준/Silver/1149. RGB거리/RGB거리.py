import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

    if i > 0:
        l[i][0] += min(l[i-1][1], l[i-1][2])
        l[i][1] += min(l[i-1][0], l[i-1][2])
        l[i][2] += min(l[i-1][0], l[i-1][1])
print(min(l[n-1]))