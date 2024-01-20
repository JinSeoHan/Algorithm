'''
1. dp[i] : 총 i번 눌러서 만들 수 있는 A의 최대개수

2. 아이디어 : "선택" > "복사" > "붙여넣기" 과정을 끝마치고 
            "붙여넣기"를 반복해서 나올 수 있는 값 중 가장 큰 값를 dp[i]에 저장

3. ex) dp[5] = max(dp[6-3)*2, dp[6-4]*3, dp[6-5]*4])
        dp[6-3]*2 : dp[3]을 복사해서 붙여넣기 한번 수행 값 dp[3]*2
        dp[6-4]*3 : dp[2] 복사해서 붙여넣기만 수행한 값 dp[2]*3

4. 하지만 n=6 까지는 복사한 값을 연속해서 붙여넣는 방식으로 이득을 볼 수 없음 -> 그냥 A를 출력하는게 젤 효율적임
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(101)

# 1~6까지는 복사해서 붙여넣는 방식보다 그냥 A붙이는게 효율적
for i in range(1, 7): 
    dp[i] = i

# 7~n까지는 복사한 값을 반복해서 붙이는 요소들 중 가장 큰 값을 저장
for i in range(7, n+1):
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i-j]*(j-1))
print(dp[n])