import sys
input = sys.stdin.readline

n = int(input())
l = [[0] * 10 for i in range(n+1)]
for i in range(1, 10):
    l[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            l[i][j] = l[i-1][j+1]
        elif j == 9:
            l[i][j] = l[i-1][j-1]
        else:
            l[i][j] = (l[i-1][j-1] + l[i-1][j+1]) % 1000000000
print(sum(l[n])%1000000000)
