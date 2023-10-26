oneCnt = 0
zeroCnt = 0
def solution(arr):
    f(arr, 0, len(arr)-1, 0, len(arr)-1)
    return zeroCnt, oneCnt
    
def f(arr, rs, re, cs, ce):
    global oneCnt, zeroCnt
    if rs==re and cs==ce:
        if arr[rs][cs] == 1:
            oneCnt += 1 
        else:
            zeroCnt += 1
        return
    
    if oneCheck(arr, rs, re, cs, ce):
        oneCnt += 1
        return
    elif zeroCheck(arr, rs, re, cs, ce):
        zeroCnt += 1
        return
    
    f(arr, rs, (rs+re)//2, cs, (cs+ce)//2)#왼위
    f(arr, rs, (rs+re)//2, (cs+ce)//2+1, ce)#오위
    f(arr, (rs+re)//2+1, re, cs, (cs+ce)//2)#왼아
    f(arr, (rs+re)//2+1, re, (cs+ce)//2+1, ce)
    
def oneCheck(arr, rs, re, cs, ce):
    for r in range(rs, re+1):
        for c in range(cs, ce+1):
            if arr[r][c] != 1:
                return False
    return True
def zeroCheck(arr, rs, re, cs, ce):
    for r in range(rs, re+1):
        for c in range(cs, ce+1):
            if arr[r][c] != 0:
                return False
    return True