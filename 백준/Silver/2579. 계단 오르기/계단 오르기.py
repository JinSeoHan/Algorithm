import sys
input = sys.stdin.readline

n = int(input())
l = [[0] * 3 for row in range(n+1)]

num = int(input())
l[1][0], l[1][1], l[1][2] = num, num, num
for i in range(2, n + 1):
    l[i][0] = int(input())
    #점프해서 올 수 있는 최선의 값
    l[i][1] = l[i][0] + max(l[i-2][1], l[i-2][2])
    #점프하지 않고 올 수 있는 최선의 값
    l[i][2] = l[i-1][1] + l[i][0]

print(max(l[n]))