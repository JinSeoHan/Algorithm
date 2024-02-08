import sys 
input = sys.stdin.readline

s, n = input().split()
s = int(s)

length = len(n)
board = [[' ']*(length*(s+2) + length) for row in range(2*s+3)]

posDic = {
    '1':(3,6), 
    '2':(1,3,4,5,7), 
    '3':(1,3,4,6,7),
    '4':(2,3,4,6),
    '5':(1,2,4,6,7),
    '6':(1,2,4,5,6,7),
    '7':(1,3,6),
    '8':(1,2,3,4,5,6,7),
    '9':(1,2,3,4,6,7),
    '0':(1,2,3,5,6,7)
}

r, c = 0, 0
for num in n:
    for pos in posDic[num]:
        if pos == 1:
            for i in range(s):
                board[r][c+1+i] = '-'
        elif pos == 2:
            for i in range(s):
                board[r+1+i][c] = '|'
        elif pos == 3:
            for i in range(s):
                board[r+1+i][c+s+1] = '|'
        elif pos == 4:
            for i in range(s):
                board[r+s+1][c+1+i] = '-'
        elif pos == 5:
            for i in range(s):
                board[r+s+2+i][c] = '|'
        elif pos == 6:
            for i in range(s):
                board[r+s+2+i][c+s+1] = '|'
        elif pos == 7:
            for i in range(s):
                board[r+2*s+2][c+1+i] = '-'
    c += s+2+1

for r in board:
    for c in r:
        print(c, end='')
    print()