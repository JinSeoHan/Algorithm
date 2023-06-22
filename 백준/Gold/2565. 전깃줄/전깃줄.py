import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l = sorted(l)
lis = [l[0][1]]
for i in range(1, n):
    if l[i][1] > lis[-1]:
        lis.append(l[i][1])
    else:
        for j, v in enumerate(lis):
            if v >= l[i][1]:
                lis[j] = l[i][1]
                break
print(len(l) - len(lis))