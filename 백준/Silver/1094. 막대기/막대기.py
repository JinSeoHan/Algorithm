x = int(input())
l1 = 64
result = 0
cnt = 0
while result != x:
    if result + l1 > x:
        l1 /= 2
        continue
    else:
        result += l1
        cnt += 1
print(cnt)