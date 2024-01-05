import sys
input = sys.stdin.readline

n = int(input())

sum = 0
number = 0
while sum < n:
    number += 1
    sum += number
print(number) if sum == n else print(number-1)