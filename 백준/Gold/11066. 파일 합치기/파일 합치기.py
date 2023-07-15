import sys
input = sys.stdin.readline

def getMinCost(l : list) -> int:
    cost = [[0]*(len(l)) for r in range(len(l))]

    #범위 합을 빠르게 찾기 위한 누적합을 찾음
    sums = [0]
    for i in range(1, len(l)):
        sums.append(sums[i-1] + l[i])

    #s~e까지의 cost를 찾음
    for diff in range(1, len(l)):#범위 크기
        s = 1
        e = s + diff

        while e < len(l):
            cost[s][e] = 10000000000
            for i in range(s,e):
                cost[s][e] = min(cost[s][e], cost[s][i]+cost[i+1][e] + sums[e] - sums[s-1])

            s += 1
            e = s + diff

    return cost[1][len(l)-1]

for _ in range(int(input())):
    k = int(input())
    l = [0] + list(map(int, input().split()))
    print(getMinCost(l))