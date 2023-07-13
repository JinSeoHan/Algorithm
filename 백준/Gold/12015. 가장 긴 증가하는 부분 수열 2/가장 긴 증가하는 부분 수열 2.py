import sys
input = sys.stdin.readline

def getchngPos(l : list, v : int) -> int:
    lo, hi = 0, len(l) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if v <= l[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi + 1


a = int(input())
l = list(map(int, input().split()))

memo = l[:1]
for i in range(1, a):#수열의 각 값
    if  l[i] > memo[-1]:# 큰값이면 끝에 저장
        memo.append(l[i])
        continue

    #찾는 과정
    pos = getchngPos(memo, l[i])
    memo[pos] = l[i]
    
print(len(memo)) 