import sys
input = sys.stdin.readline

mod = 1000000007
def mul(m1 : list, m2 : list) -> list:
    m1RC, m1CC, m2CC = len(m1), len(m1[0]),len(m2[0])
    r = []
    for i in range(m1RC):
        r.append([])
        for j in range(m2CC):
            sum = 0
            for k in range(m1CC):
                sum += m1[i][k]*m2[k][j]%mod
            r[i].append(sum%mod)
    return r
                
def fibo6(n):
    global u
    if n == 1:
        return u
    fibo6(n//2)
    if n % 2 == 0:
        u = mul(u, u)
    else:
        u = mul(mul(u, u), orgU)
    return u

num = int(input())
u = [[1, 1], [1, 0]]
orgU = u.copy()
print(fibo6(num)[1][0])