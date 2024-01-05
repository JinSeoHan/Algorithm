n = int(input())
sum, number = 0, 0
while sum <= n:
    number += 1
    sum += number
print(number-1)