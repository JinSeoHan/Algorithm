'''
1 <= N <= 1000 이므로 N^2까지 가능함
현재 보드블록 위치로 점프할 수 있는 모든 블록을 탐색하여 가장 비용이 적은 값을 찾아 업데이트
'''
import sys
input = sys.stdin.readline

INF = 10000000

n = int(input())
block = [None] + list(input())

dp = [INF]*(n+1)
dp[1] = 0

def getPrevBlock(b):
    prevBlcok = None
    if b == 'B':
        prevBlcok = 'J'
    elif b == 'O':
        prevBlcok = 'B'
    elif b == 'J':
        prevBlcok = 'O'
    return prevBlcok

for i in range(2, n+1):
    currblock = block[i] # 현재 블록
    prevBlcok = getPrevBlock(currblock) # 이전 블록
    for j in range(1, i):
        if block[j] == prevBlcok:
            dp[i] = min(dp[i], dp[j]+(i-j)**2)

print(-1) if dp[n]==INF else print(dp[n])