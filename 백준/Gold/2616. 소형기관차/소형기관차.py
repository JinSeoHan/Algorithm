'''
dp를 소형 기관차 번호 순서대로 총 3번을 함
1. 1번 소형 기관차의 최대 승객수 찾음
2. 1, 2번 소형 기관차에 실을 수 있는 최대 승객 수 찾음
3. 1, 2, 3번 소형 기관차에 실을 수 있는 최대 승객 수 찾음

dp[i][j] : 1~i번째 소형기관차에 j번 객실까지 고려해서 운송할 수 있는 최대 승객 수
'''
import sys
input = sys.stdin.readline

n = int(input()) # 객차의 개수
l = [0] + list(map(int, input().split())) # 객차의 인원 수
m = int(input()) # 소형 기관차가 끌 수 있는 객차의 개수

dp = [[0]*(n+1) for row in range(4)] # dp[i][j] : i번 소형 기관차가 j객차 까지 고려하여 운송할 수 있는 최대 승객 수 
arr = [0] # i 객차 까지의 승객 수 누적합
for i in l[1:]:
    arr.append(arr[-1]+ i)


for i in range(1, 4):
    for j in range(i*m, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + arr[j]-arr[j-m])
print(dp[3][n])