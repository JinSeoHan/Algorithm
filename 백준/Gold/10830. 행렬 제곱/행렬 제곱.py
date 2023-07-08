import sys
input = sys.stdin.readline

def maMul(m1 : list, m2 : list):
    m1RowCnt = len(m1)
    m1ColCnt = len(m1[0])
    m2ColCnt = len(m2[0])

    r = []
    for i in range(m1RowCnt):
        r.append([])
        for j in range(m2ColCnt):
            sum = 0
            for k in range(m1ColCnt):
                sum += m1[i][k]*m2[k][j]
            r[i].append(sum%1000)
    return r

def square(n):
    global m
    if n == 1:
        for i in range(len(m)):
            for j in range(len(m[0])):
                m[i][j] %= 1000
        return

    square(n//2)
    if n % 2 == 0:
        m = maMul(m, m)
    else:
        m = maMul(m, m)
        m = maMul(m, orgnM)

n, b = map(int, input().split())
m = []
orgnM = []

for i in range(n):
    m.append(list(map(int, input().split())))
orgnM = m.copy()

square(b)

for i in range(n):
    print(*m[i])