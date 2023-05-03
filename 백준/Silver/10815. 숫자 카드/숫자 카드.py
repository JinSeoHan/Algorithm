import sys
input = sys.stdin.readline

result = [0] * 20000001
n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

for i in nArr:
    result[i] = 1

for i in mArr:
    print(result[i], end=' ')