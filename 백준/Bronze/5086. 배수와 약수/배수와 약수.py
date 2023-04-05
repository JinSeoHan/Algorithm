a, b = map(int, input().split())
while (a, b) != (0, 0):
    if a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    else:
        if b % a == 0:
            print('factor')
        else:
            print('neither')
    a, b = map(int, input().split())