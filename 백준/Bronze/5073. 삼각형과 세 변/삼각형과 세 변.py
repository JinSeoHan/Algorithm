import sys
arr = list(map(int, sys.stdin.readline().split()))
while sum(arr) != 0:
    arr.sort()

    if arr[0] + arr[1] <= arr[2]:
        print('Invalid')
    elif arr[0] == arr[1] == arr[2] and arr[0] == arr[2]:
        print('Equilateral')
    elif arr[0] != arr[1] != arr[2] and arr[0] != arr[2]:
        print('Scalene')
    else:
        print('Isosceles')
    arr = list(map(int, sys.stdin.readline().split()))