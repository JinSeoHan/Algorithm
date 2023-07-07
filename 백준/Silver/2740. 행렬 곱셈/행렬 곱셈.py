import sys
input = sys.stdin.readline

m = []
result = []
for mc in range(2):
    m.append([])
    r, c = map(int, input().split())
    for i in range(r):
        m[mc].append(list(map(int, input().split())))

for i in range(len(m[0])):#matrix1번의 행개수
    result.append([])
    for j in range(len(m[1][0])):#matrix2번의 열개수
        sum = 0
        for k in range(len(m[0][0])):#matrix1번 열개수
            sum += m[0][i][k]*m[1][k][j]
        result[i].append(sum)

for i in range(len(result)):
    print(*result[i])