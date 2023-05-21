import sys
input = sys.stdin.readline

n = int(input())
lArr = []
pushCount = 1
resultString = list()
isNo = False
for i in range(1, n+1):
    num = int(input())

    #들어온 값이 아직 push된적이 없는 수인 경우
    if pushCount <= num:
        while pushCount <= num:
            lArr.append(pushCount)
            pushCount += 1
            resultString.append('+')

    if lArr[-1] == num:
        lArr.pop()
        resultString.append('-')
    else:
        isNo = True
        break
        
if isNo: 
    print('NO')
else:
    for i in resultString:
        print(i)