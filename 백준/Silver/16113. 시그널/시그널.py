import sys
input = sys.stdin.readline

n = int(input())
x, y = 5, n//5
arr = [['.']*(y) for r in range(x)]

# 배열에 값 저장
for i, v in enumerate(input().rstrip()):
    r = i // (n//5)
    c = i % (n//5)
    arr[r][c] = v

result = []
check = [[False]*y for row in range(x)]
# dfs로 #개수를 찾음
def dfs(check, r, c):
    check[r][c] = True
    cnt = 0
    for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr,nc = r+dir[0], c+dir[1]
        if 0 <= nr < x and 0 <= nc < y and arr[nr][nc] == '#' and not check[nr][nc]:
            cnt += dfs(check, nr, nc)
    return cnt + 1

# 배열에서 #개수 찾기
def getCount(arr, c):
    cnt = dfs(check, 0, c)
    return cnt

# 배열 해독
def getNumber(arr, c):
    cnt = getCount(arr, c)
    if cnt == 5:
        return 1
    elif cnt == 7:
        return 7
    elif cnt == 9:
        return 4
    elif cnt == 11: # 2,3,5의 #개수는 11개
        if arr[3][c] == '#':
            return 2
        elif arr[1][c] == '#':
            return 5
        else:
            return 3
    elif cnt == 12: # 0,6,9의 #개수는 12개
        if arr[1][c+2] == '.':
            return 6
        elif arr[3][c] == '.':
            return 9
        else:
            return 0
    elif cnt == 13:
        return 8


for c in range(y):
    # 시작점을 찾음
    if arr[0][c] == '#' and not check[0][c]:
        result.append(getNumber(arr, c))

# 결과 출력
for v in result:
    print(v, end='')