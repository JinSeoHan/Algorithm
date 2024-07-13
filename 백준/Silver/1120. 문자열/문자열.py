import sys
input = sys.stdin.readline

a, b = input().split()

result = 50
for sIdx in range(len(b)-len(a)+1):
    diffCnt = 0
    for idx in range(sIdx, sIdx+len(a)):
        if a[idx-sIdx] != b[idx]:
            diffCnt += 1
    result = min(result, diffCnt)
print(result)