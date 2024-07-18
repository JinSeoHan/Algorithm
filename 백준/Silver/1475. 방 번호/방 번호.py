from math import ceil
n = list(map(int, input().strip()))

memo = [0]*10
for v in n:
    memo[v] += 1

result = 0
for i, v in enumerate(memo):
    if i == 6 or i == 9: continue
    result = max(result, v)
result = max(result, ceil((memo[6]+memo[9]) / 2))
print(result)