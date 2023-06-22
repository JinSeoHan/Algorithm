import sys
input  = sys.stdin.readline

n = int(input())
l0 = list(map(int, input().split()))
l1 = [0] * n
l2 = [0] * n
l1[0], l2[-1] = 1, 1

for i in range(1, n):
    max = 0
    for j in range(i):
        if l0[j] < l0[i] and l1[j] > max:
            max = l1[j]
    l1[i] = max + 1
result = 0;
for i in reversed(range(0, n-1)):
    max = 0
    for j in range(i+1, n):
        if l0[j] < l0[i] and l2[j] > max:
            max = l2[j]
    l2[i] = max + 1
    if l1[i] + l2[i] - 1 > result:
        result = l1[i] + l2[i] - 1
if n == 1:
    print(1)
else:
    print(result)