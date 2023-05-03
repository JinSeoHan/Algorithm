import sys
input = sys.stdin.readline
n = int(input())
lArr = list(map(int, input().split()))
sArr = set(lArr)#중복제거
sArr = sorted(sArr)#오름차순 정렬
dic = {}
for i in range(len(sArr)):
    dic[sArr[i]] = i
for i in lArr:
    print(dic[i], end=' ')