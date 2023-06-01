import sys
input = sys.stdin.readline

def fillStar(n : int, x : int, y : int):
    if n == 1:
        resultL[x][y] = '*'
        return 

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            fillStar(n//3, x + (n//3)*i, y + (n//3)*j)
            
n = int(input())
resultL = []
for i in range(n):
    resultL.append([' ']*n)

fillStar(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(resultL[i][j], end='')
    print()