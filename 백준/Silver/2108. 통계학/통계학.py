import math
import sys
input = sys.stdin.readline

def realRound(num : float) -> int:
    a = math.trunc(num)#정수부
    b = num-a#소수부
    if num > 0:
        if b >= 0.5:
            return a+1
        else:
            return a
    elif num < 0:
        if b <= -0.5:
            return a-1
        else:
            return a
    else:
        return 0
    
n = int(input())
lArr = list()
dic = dict()
for _ in range(n):
    num = int(input())
    lArr.append(num)
    if num in dic:
        dic[num] += 1
        isNever = False
    else:
        dic[num] = 0

#산술평균
print(realRound(sum(lArr)/n))
#중앙값
sortedLArr = sorted(lArr)
print(sortedLArr[n//2])
#최빈값
dic = sorted(dic.items(), key=lambda x : (x[1], x[0]))
isPrint = False
for i in range(len(dic)-1,-1,-1):
    if dic[i][1] != dic[-1][1]:
        if i+2 <= len(dic)-1:
            print(dic[i+2][0])
            isPrint =True
            break
        else:
            print(dic[-1][0])
            break
    if i == 0:
        if n == 1:
            print(lArr[0])
        else:
            print(dic[1][0])
#범위
print(sortedLArr[-1] - sortedLArr[0])