import sys
input = sys.stdin.readline

n = int(input())
board = []
visited = [[0]*n for row in range(n)]
visited[0][0] = 1


def validate(i, j):
    return 0 <= i < n and 0 <= j < n

for i in range(n): # 행
    for j, v in enumerate(list(map(int, input().split()))): # 열, 행열값
        # 오른쪽, 아래 순서
        if visited[i][j] == 0 or v == 0: continue
        for pos in [(0,1),(1,0)]:
            ni, nj = i+pos[0]*v, j+pos[1]*v
            if validate(ni, nj):
                visited[ni][nj] += visited[i][j]

print(visited[-1][-1])