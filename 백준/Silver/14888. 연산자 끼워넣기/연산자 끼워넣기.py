import sys
input = sys.stdin.readline

def dfs(sum, nextNumIdx):
    #종료조건
    if nextNumIdx == n:
        result.append(sum)
        return

    #연산을 수행함
    for i in range(n-1):
        #사용된 연산자 넘어감
        if useCheck[i] == True:
            continue

        useCheck[i] = True
        
        dfs(operation(sum, nums[nextNumIdx], opers[i]), nextNumIdx + 1)
        useCheck[i] = False

def operation(a, b, oper):
    if oper == 0:
        return a + b
    elif oper == 1:
        return a - b
    elif oper == 2:
        return a * b
    elif oper == 3:
        if a < 0 and b > 0:
            return -(-a // b)
        return a // b
        

n = int(input())
nums = list(map(int, input().split()))
operNums = list(map(int, input().split()))
opers = []
for i in range(4):
    if i == 0:
        opers += [0] * operNums[i]
    elif i == 1:
        opers += [1] * operNums[i]
    elif i == 2:
        opers += [2] * operNums[i]
    elif i == 3:
        opers += [3] * operNums[i]

useCheck = [False] * (n-1)#사용된 연산자 기록
result = []
dfs(nums[0], 1)
print(max(result))
print(min(result))