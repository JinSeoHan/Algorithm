n, k = map(int, input().split())

nP = 1;
for _ in range(k):
    nP *= n
    n -= 1
kP = 1 ;
for i in range (1, k+1):
    kP *= i

print(nP//kP)