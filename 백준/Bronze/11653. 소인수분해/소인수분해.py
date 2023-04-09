import sys
n = int(sys.stdin.readline())
i = 2
if n == 1:
    exit()
while n != 1:
    while n % i == 0:
        print(i)
        n //= i
    i += 1