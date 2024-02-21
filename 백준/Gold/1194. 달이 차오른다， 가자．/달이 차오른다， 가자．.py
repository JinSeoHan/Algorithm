'''
비트마스크를 활용하여 소유하고 있는 키를 나타냄
a : 000001, b:000010, c:000100, d:001000, e:010000, b:100000
"mykey = 011011" : a,b,d,e 키를 가지고 있다는 의미

visited[i][j][myKey] : 소유중인 열쇠를 가지고 i, j 위치를 방문하였는지 기록

최단거리를 찾아야하기 때문에 BFS 사용
queue에는 visited된 위치 값이 들어가면 안되기 때문에 append전에 True 체크
-> popleft() 아래에서 True 설정시 중복된 위치값이 queue에 들어가 시간초과
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(input().rstrip()) for _ in range(n)]
keys = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}
doors = {'A':1,'B':2,'C':4,'D':8,'E':16,'F':32}
visited = [[[False]*64 for c in range(m)] for r in range(n)]


def isValid(i, j, myKey):
    return 0 <= i < n and 0 <= j < m and field[i][j] != '#' and not visited[i][j][myKey]
def bfs(i, j):
    global visited
    queue = deque()
    queue.append((i,j,0,0)) # x좌표,y좌표,비트마스크(소유중인키값),이동거리
    visited[i][j][0] = True
    field[i][j] = '.'

    while queue:
        ci, cj,cMyKeys,cDist = queue.popleft()

        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni, nj = ci+dir[0], cj+dir[1]
            if isValid(ni, nj, cMyKeys): # 바운더리, '#'위치, 방문검사
                match field[ni][nj]:
                    # 통로인 경우
                    case '.':
                        visited[ni][nj][cMyKeys] = True
                        queue.append((ni,nj,cMyKeys,cDist+1))
                    # 열쇠 위치인 경우
                    case v if v in keys:
                        newMyKeys = cMyKeys | keys[v]
                        if not visited[ni][nj][newMyKeys]:
                            visited[ni][nj][newMyKeys] = True
                            queue.append((ni,nj,newMyKeys,cDist+1))
                    # 문 위치인 경우
                    case v if v in doors:
                        if cMyKeys & doors[v]:
                            visited[ni][nj][cMyKeys] = True
                            queue.append((ni,nj,cMyKeys,cDist+1))
                    # 출구인 경우
                    case '1':
                        return cDist+1
    return -1

# 0의 위치에서 출발하여 결과 출력
for i in range(n):
    for j in range(m):
        if field[i][j] == '0':
            print(bfs(i,j))
            exit(0)