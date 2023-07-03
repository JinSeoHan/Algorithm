import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(input().rstrip()))

def quadTree(r, c, l):
    v = arr[r][c]
    
    for i in range(r, r+l):
        for j in range(c, c+l):
            if arr[i][j] != v:
                print('(', end='')
                quadTree(r, c, l//2)
                quadTree(r, c+l//2, l//2)
                quadTree(r+l//2, c, l//2)
                quadTree(r+l//2, c+l//2, l//2)
                print(')', end='')
                return
    print(v, end='')

quadTree(0, 0, n)