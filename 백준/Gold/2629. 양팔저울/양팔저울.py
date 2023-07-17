import sys
input = sys.stdin.readline

chuCnt = int(input())
chuL = list(map(int, input().split()))
guCnt = int(input())
guL = list(map(int, input().split()))
result = ['N']*guCnt

wL = set()
wL.add(0)
for i, chuV in enumerate(chuL):
    #추 i개로 만들 수 있는 무게 리스트
    temp = set()
    for w in wL:
        temp.add(abs(w+chuV))
        temp.add(abs(chuV-w))
    wL |= temp
    for idx, guV in enumerate(guL):
        if guV in wL:
            result[idx] = 'Y'
print(' '.join(result))