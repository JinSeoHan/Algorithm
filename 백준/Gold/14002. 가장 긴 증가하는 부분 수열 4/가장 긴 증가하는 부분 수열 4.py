import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

dpLen = [0]
for i in range(1, n):
    if result[-1] < arr[i]:
        result.append(arr[i])
        dpLen.append(len(result)-1)
        continue
    
    for j in range(len(result)):
        if arr[i] <= result[j]:
            result[j] = arr[i]
            dpLen.append(j)
            break
length = len(result)
cnt = length -1

ans = []
for i in reversed(range(n)):
    if dpLen[i] == cnt:
        ans.append(arr[i])
        cnt -= 1

print(length)
print(*list(reversed(ans)))