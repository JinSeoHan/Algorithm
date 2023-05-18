import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dicResult = dict()
for i in range(n):
    s = input().strip('\n')
    # m보다 길이가 짧으면 째낏
    if len(s) < m:
        continue
    
    if s in dicResult.keys():
        dicResult[s] += 1
    else:
        dicResult[s] = 1
dic = sorted(dicResult.items(), key=lambda x : (x[1], len(x[0])), reverse=True)
j = 0
newList = []
for i in range(len(dic)):
    if dic[i][1]==dic[j][1] and len(dic[i][0])==len(dic[j][0]):
        newList.append(dic[i][0])
    else:
        newList.sort()
        for k in newList:
            print(k)
        newList = []
        newList.append(dic[i][0])
        j = i
newList.sort()
for i in newList:
    print(i)