x, y = map(int, input().split())
result = []
board = []

for _ in range(x):
    board.append(input())

count1 = 0
count2 = 0
for i in range(x-7):
    for j in range(y-7):
        count1 = 0
        count2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a+b) % 2 == 0 and board[a][b] != 'B':
                        count1 += 1
                elif (a+b) % 2 == 0 and board[a][b] != 'W':
                        count2 += 1
                elif board[a][b] != 'W':
                        count1 += 1
                elif board[a][b] != 'B':
                        count2 += 1
        result.append(count1)
        result.append(count2)
print(min(result))