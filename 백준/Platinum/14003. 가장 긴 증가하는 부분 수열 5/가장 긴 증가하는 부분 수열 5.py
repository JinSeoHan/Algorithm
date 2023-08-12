import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ordMem = []

mem = [arr[0]]
for i in range(n):
    if mem[-1] < arr[i]:
        mem.append(arr[i])
        ordMem.append(len(mem)-1)
        continue
    
    l, r = 0, len(mem) -1
    while l <= r:
        mid = (l + r) // 2
        if arr[i] > mem[mid]:
            l = mid + 1
        else:
            r = mid - 1
    # if r == -1:
    #     r = 0
    mem[r+1] = arr[i]
    ordMem.append(r+1)

idx = len(mem) - 1
ans = []
for i in range(n-1,-1,-1):
    if ordMem[i] == idx:
        ans.append(arr[i])
        idx -= 1

print(len(mem))
print(*ans[::-1])