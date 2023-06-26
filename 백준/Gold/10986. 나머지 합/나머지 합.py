import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
remain = [0] * m

for i in a:
    sum += i
    remain[sum%m] += 1
count = 0
#나머지가 같은 수중 2개를 고르는 경우의수
for i in remain:
    count += i*(i-1)//2
print(count+remain[0])