'''
dp[s][a][b][c] : s곡을 dotorya가 a번 kesakiyo가 b번 hongjun7 c번 부를 때 만들 수 있는 앨범의 종류

dp[0][0][0][0]에서 a, b, c, ab, bc, ac, abc가 노래를 부르는 경우를 추가하여 업데이트

ex) dp[3][1][1][1] == ??
[dp[0][0][0][0]에서 노래를 부르는 경우 업데이트]
    <a가 노래를 부르는 경우>
        dp[1][1][0][0] += dp[0][0][0][0]
    <b가 노래를 부르는 경우>
        dp[1][0][1][0] += dp[0][0][0][0] 
    ...
    <abc가 함께 노래를 부르는 경우>
        dp[1][1][1][1] += dp[0][0][0][0]
    ==> dp[0][0][0][0] 으로 만들어 질 수 있는 모든 경우의 수를 다 찾음
[dp[1][1][0][0]에서 노래를 부르는 경우 업데이트]
...
[dp[3][1][1][1]에서 노래를 부르는 경우 업데이트]


'''
import sys
from collections import deque
input = sys.stdin.readline

s, a, b, c = map(int, input().split())
dp = [[[[0]*51 for b in range(51)] for a in range(51)] for s in range(51)]
dp[0][0][0][0] = 1

def acka():
    queue = deque()
    queue.append((0,0,0,0))
    while queue:
        cs, ca, cb, cc = queue.popleft()
        if cs==s and ca==a and cb==b and cc==c: break

        for case in [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]:
            ns, na, nb, nc = cs+1, ca+case[0], cb+case[1], cc+case[2]
            if ns > s or na > a or nb > b or nc > c: continue

            # ns,na,nb,nc는 큐에 딱 한번만 들어가야함
            if not dp[ns][na][nb][nc]:
                queue.append((ns,na,nb,nc))
            dp[ns][na][nb][nc] += dp[cs][ca][cb][cc] 
            dp[ns][na][nb][nc] %= 1000000007

    return dp[s][a][b][c]

print(acka())