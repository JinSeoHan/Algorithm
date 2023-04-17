n = int(input())

x, y = 0, 1
while n > 0:
    if n % 5 == 0:
        x = n // 5
        n = 0
        break
    n -= 3
    y += 1
if n == 0:
    print(x+y-1)
else:
    print(-1)