import sys
input = sys.stdin.readline
arr = [2]

def isprim(num):
    result = True
    if num in arr:
        return True
    elif num == 1:
        return False
    else:
        for i in arr:
            if num % i == 0:
                result = False
                break
        for i in range(arr[-1], num):
            if num % i == 0:
                result = False
                break
    if result:
        arr.append(num)
    return result

N = int(input())
number = list(map(int, input().split()))
count = 0
for e in range(1, 1001):
    isprim(e)
for i in number:
    if i in arr:
        count += 1
print(count)