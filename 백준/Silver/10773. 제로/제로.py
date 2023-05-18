import sys
input = sys.stdin.readline

n = int(input())

lArr = list()
for i in range(n):
    n = int(input())
    if n == 0 and len(lArr) != 0:
        lArr.pop()
    else:
        lArr.append(n)

print(sum(lArr))