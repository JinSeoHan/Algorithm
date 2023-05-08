import sys
input = sys.stdin.readline

dic = dict()
n = int(input())
for i in map(int, input().split()):
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
m = int(input())
for i in map(int, input().split()):
    if i in dic.keys():
        print(dic[i], end=' ')
    else:
        print(0, end=' ')