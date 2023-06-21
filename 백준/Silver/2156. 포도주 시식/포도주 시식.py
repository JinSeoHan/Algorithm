import sys
input = sys.stdin.readline

n = int(input())
l = [[0] * 2 for i in range(n+1+3)]
for i in range(4):
    l[i][0], l[i][1] = 0, 0
for i in range(4, n+1+3):
    l[i][0] = int(input())
    #현재 잔을 마셨을 경우
    l[i][1] = max(l[i-3][1] + l[i-1][0] + l[i][0], l[i-2][1] + l[i][0])
    #안마셨을 경우
    l[i][1] = max(l[i][1], l[i-1][1])    
print(l[n+3][1])