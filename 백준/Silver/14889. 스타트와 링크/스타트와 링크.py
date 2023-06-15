import sys
input = sys.stdin.readline

n = int(input())
arr = []
check = [False] * n
for i in range(n):
    arr.append(list(map(int, input().split())))

checkedNums = []
teams = []
flag = False
minDiff = 1000000000
def dfs(nextIdx):
    global minDiff
    if len(checkedNums) == n//2:

        sum1 = 0
        sum2 = 0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    sum1 += arr[i][j]
                elif not check[i] and not check[j]:
                    sum2 += arr[i][j]
        minDiff = min(minDiff, abs(sum1-sum2))
        return

    for i in range(n):
        if i < nextIdx:
            continue

        check[nextIdx] = True
        checkedNums.append(i)
        dfs(i + 1)
        checkedNums.pop()
        check[nextIdx] = False

dfs(0)
print(minDiff)