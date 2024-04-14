# 키보드 입력
keyboard = []
keyboard.append(list('qwertyuiop'))
keyboard.append(list('asdfghjkl'))
keyboard.append(list('zxcvbnm'))

ls, rs = input().split()

# 자음인지
def isConsonant(c):
    return c in 'qwertasdfgzxcv'

def findPos(k):
    for i, r in enumerate(keyboard):
        for j, v in enumerate(r):
            if k == v:
                return i, j

def getTime(i, j , ii, jj):
    return  abs(i-ii) + abs(j-jj) + 1

csi, csj = findPos(ls) # 시작 자음
vsi, vsj = findPos(rs) # 시작 모음
totalTime = 0
for v in input():
    if isConsonant(v):
        ci, cj = findPos(v)
        totalTime += getTime(csi,csj,ci,cj)
        csi,csj = ci, cj
    else:
        vi, vj = findPos(v)
        totalTime += getTime(vsi,vsj,vi,vj)
        vsi, vsj = vi, vj
print(totalTime)