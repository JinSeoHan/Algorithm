import sys
input = sys.stdin.readline

def caseCount(w : int, e : int) -> int:

    wNum = 1
    for i in range(1, w+1):
        wNum *= i
    eNum = 1
    for _ in range(w):
        eNum *= e
        e -= 1
    return eNum // wNum

n = int(input())
for _ in range(n):
    w, e = map(int, input().split())
    print(caseCount(w, e))