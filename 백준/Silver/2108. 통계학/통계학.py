import sys
input = sys.stdin.readline
 
n = int(input())
lArr = [0] * 8001

sum = 0
for _ in range(n):
    num = int(input())

    #산술평균용
    sum += num
    #최빈값용
    lArr[num] += 1

inputList = list()
maxList = list()
maxValue = max(lArr)
for i in range(-4000,4001):
    if lArr[i] > 0:
        #중앙값용
        for j in range(lArr[i]):
            inputList.append(i)
        #최빈값용
        if lArr[i] == maxValue:
            maxList.append(i)

dic = dict()

#산술평균
a = (sum/n)-(sum//n)#소수부분
if a < 0:
    if a <= -0.5:
        print((sum//n)-1)
    else:
        print(sum//n)
else:
    if a >= 0.5:
        print((sum//n)+1)
    else:
        print(sum//n)

#중앙값
print(inputList[n//2])
#최빈값
if len(maxList) == 1:
    print(maxList[0])
else:
    print(maxList[1])
#범위
print(inputList[-1] - inputList[0])