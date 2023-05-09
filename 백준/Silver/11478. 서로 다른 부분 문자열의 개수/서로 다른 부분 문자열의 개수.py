import sys
input = sys.stdin.readline
s = input()
sLen = len(s)
rSet = set()
for i in range(1,sLen+1):#쪼갤 문자열 개수
    for j in range(sLen):#시작 문자 인덱스
        if i+j > sLen-1:
            break
        rSet.add(s[j:j+i])
print(len(rSet))