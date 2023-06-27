import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[0] * (n+1)]
for i in range(n):
    l.append([0] + list(map(int, input().split())))
    for j in range(1, n+1):#1,1 x,x 합을 x,x에 저장
        l[-1][j] += l[-2][j] + l[-1][j-1] - l[-2][j-1]
for i in range(m):
    x1,y1, x2,y2 = map(int, input().split())
    print(l[x2][y2] - l[x1-1][y2] - l[x2][y1-1] + l[x1-1][y1-1])