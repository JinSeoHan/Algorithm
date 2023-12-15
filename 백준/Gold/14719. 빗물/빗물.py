import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = list(map(int, input().split()))

#2차원 세계 그리기
matrix = [[0]*m for row in range(n)]
for col in range(m):
    for row in range(n-1, n-h[col]-1, -1):
        matrix[row][col ] = 1

result = 0
#밑에서 위 순서로 빗물값 찾음
for row in range(n-1, -1, -1):
    b, w = False, False
    rain = 0
    #좌에서 우로 빗물값 찾음
    for col in range(m):
        v = matrix[row][col]

        #벽을 만난 순간 기록된 빗물값을 저장
        if v == 1:
            b = True
            w = False
            result += rain
            rain = 0
        elif v == 0:
            w = True
        
        if b and w: rain += 1
print(result)