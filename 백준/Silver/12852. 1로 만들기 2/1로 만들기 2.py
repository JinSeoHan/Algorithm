import sys
input = sys.stdin.readline

N = int(input())
dp = [(0, [1]), (0, [1])]

for i in range(2, N+1):
    case = [(dp[i-1][0], i-1)]
    if i % 3 == 0:
        case.append((dp[i//3][0], i//3))
    if i % 2 == 0:
        case.append((dp[i//2][0], i//2))
    minCostIndexTuple = min(case)

    minCost = minCostIndexTuple[0]
    minIdx = minCostIndexTuple[1]
    minGraph = dp[minIdx][1].copy()

    minGraph.append(i)
    dp.append((minCost+1,minGraph))

print(dp[N][0])
print(*dp[N][1][::-1])