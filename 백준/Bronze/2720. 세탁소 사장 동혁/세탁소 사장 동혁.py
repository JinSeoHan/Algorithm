n = int(input())
money = [25, 10, 5, 1]
res = [0] * 4

for i in range(n):
    n = int(input())
    for j in range(4):
        res[j] = n // money[j]
        n %= money[j]
    print(*res)