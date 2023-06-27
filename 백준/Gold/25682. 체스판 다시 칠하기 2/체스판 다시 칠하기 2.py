import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
b = [[0] * (m+1) for i in range(n+1)]
w = [[0] * (m+1) for i in range(n+1)]
minimum = n * m + 1

for i in range(1, n+1):
    l = list(input())
    for j in range(1, m+1):
        b[i][j] = b[i-1][j] + b[i][j-1] - b[i-1][j-1]
        w[i][j] = w[i-1][j] + w[i][j-1] - w[i-1][j-1]

        if (i+j)%2 == 0:
            if l[j-1] == 'B':
                w[i][j] +=1
            else:
                b[i][j] +=1
        else:
            if l[j-1] == 'B':
                b[i][j] +=1
            else:
                w[i][j] +=1

        if i >= k and j >= k:
            r1 = b[i][j] - b[i-k][j] - b[i][j-k] + b[i-k][j-k]
            r2 = w[i][j] - w[i-k][j] - w[i][j-k] + w[i-k][j-k]
            minimum = min(minimum, r1, r2)
print(minimum)