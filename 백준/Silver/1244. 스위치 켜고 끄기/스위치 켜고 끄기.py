import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
for i in range(int(input())):
    gender, pos = map(int, input().split())
    if gender == 1:
        cnt = 1
        npos = pos
        while npos <= n:
            l[npos-1] = 0 if l[npos-1] else 1
            cnt += 1
            npos = pos * cnt
    else:
        cnt = 0
        l[pos-cnt-1] = 0 if l[pos-cnt-1] else 1 # 첫번째 연산 처리
        while 1 <= pos-cnt and pos+cnt <=n:
            if l[pos-cnt-1] == l[pos+cnt-1]:
                l[pos-cnt-1] = 0 if l[pos-cnt-1] else 1
                l[pos+cnt-1] = 0 if l[pos+cnt-1] else 1
                cnt += 1
            else: break

for v in l:
    print(v)