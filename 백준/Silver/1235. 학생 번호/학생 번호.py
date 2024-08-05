import sys
input = sys.stdin.readline

n = int(input())
idList = []
for _ in range(n):
    idList.append(input().strip())

cnt = 0
for i in range(len(idList[0])):
    start = len(idList[0])-(i+1)
    end = len(idList[0])

    temp = set()
    flag = False
    for id in idList:
        result = id[start:end]
        if result in temp:
            flag = True
            cnt += 1
            break
        temp.add(result)
    if not flag:
        print(cnt+1)
        break