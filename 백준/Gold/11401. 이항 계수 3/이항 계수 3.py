import sys
input = sys.stdin.readline

mod = 1000000007

sMemo = dict()
sMemo[0] = 1
def square(a, b):
    if b in sMemo.keys():
        return sMemo[b]
    if b == 1:
        return a

    r = 0
    if b % 2 == 0:
        r = square(a, b//2)**2%mod
    else:
        r = square(a, b//2)*square(a, b//2+1)%mod
    sMemo[b] = r
    return r

n, k = map(int, input().split())

#팩토리얼
fac = [1]
for i in range(1, n+1):        
    fac.append(i*fac[i-1]%mod) 
result = fac[n]*square(fac[k]*fac[n-k], mod-2)%mod
print(result)