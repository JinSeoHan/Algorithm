import sys
input = sys.stdin.readline

n, W = map(int, input().split())
item = [[0,0]]
cost = [[0] * (W+1) for i in range(n+1)]

for i in range(n):
    item.append(list(map(int, input().split())))
item.sort()
for i in range(1, n+1):
    for w in range(1, W+1):
        if w - item[i][0] >= 0:
            cost[i][w] = max(cost[i-1][w - item[i][0]] + item[i][1], cost[i-1][w])
        else:
            cost[i][w] = cost[i-1][w]
print(cost[-1][-1])