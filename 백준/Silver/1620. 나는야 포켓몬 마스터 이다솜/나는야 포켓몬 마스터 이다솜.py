import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nArr = []
dic = dict()

for i in range(n):
    value = input().rstrip('\n')
    nArr.append(value)
    dic[value] = int(i)

for i in range(m):
    question = input().rstrip('\n')
    if question.isnumeric():
        print(nArr[int(question)-1])
    else:
        print(int(dic[question]) + 1)