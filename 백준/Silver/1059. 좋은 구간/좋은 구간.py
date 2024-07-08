l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

minV, maxV = 0, 0

for v in s:
    if v == n:
        print(0)
        exit(0)
    if v < n:
        minV = v 
    if v > n:
        maxV = v
        break
minV, maxV = minV+1, maxV-1

result = (n-minV)*(maxV-n+1)+(maxV-n)

print(result)