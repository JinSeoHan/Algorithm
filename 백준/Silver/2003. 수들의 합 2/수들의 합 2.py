import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = list(map(int, input().split()))

s,e = 0,0

cnt = 0
sumV = q[0]
while True:
    if sumV == m:
        cnt += 1

    if sumV < m:
        e += 1
        if e == n: break
        sumV += q[e]
    elif sumV >= m:
        sumV -= q[s]
        s += 1
print(cnt)