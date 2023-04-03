n = int(input())

for _ in range(n):
    n = int(input())
    print(f'{n // 25}', end=' ')
    n = n % 25
    print(f'{n // 10}', end=' ')
    n = n % 10
    print(f'{n // 5}', end=' ')
    n = n % 5
    print(f'{n // 1}', end=' ')
    n = n % 1