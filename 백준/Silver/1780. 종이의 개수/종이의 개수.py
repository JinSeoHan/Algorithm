import sys
input = sys.stdin.readline

def paperCount(r, c, l):
    v = arr[r][c]
    for i in range(r, r+l):
        for j in range(c, c+l):
            if arr[i][j] != v:
                for k in range(3):
                    for m in range(3):
                        length = l//3
                        paperCount(r+k*length, c+m*length, length)
                return
    result[v] += 1

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = [0, 0, 0]

paperCount(0,0,n)
for i in range(-1, 2):
    print(result[i])