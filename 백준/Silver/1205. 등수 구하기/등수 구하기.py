import sys
n, score, p = map(int, input().split())
if n == 0:
    print(1)
    exit()
l = list(map(int, input().split()))

prevV = -1
cnt = 0
order = []
for v in l:
    cnt += 1
    if v == prevV:
        order.append(order[-1])
        continue
    order.append(cnt)
    prevV = v

flag = False
result = None
for i in range(n):
    if l[i] < score:
        if flag:
            result = order[i-1]
        else:
            result = order[i]
        break
    elif l[i] == score:
        flag = True

if n < p:
    if l[-1] == score:
        result = order[-1]
    elif l[-1] > score:
        result = cnt + 1
print(result) if result else print(-1)