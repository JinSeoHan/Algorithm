import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
    
    if i > 0:
        l[i][0] += l[i-1][0]
        l[i][-1] += l[i-1][-1]
        for j in range(1, len(l[i])-1):
            l[i][j] += max(l[i-1][j-1], l[i-1][j]);
print(max(l[n-1]))