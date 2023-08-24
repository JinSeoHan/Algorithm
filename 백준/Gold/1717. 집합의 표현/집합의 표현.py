import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def getParent(arr, num):
    if arr[num] == num:
        return num
    arr[num] = getParent(arr, arr[num])
    return arr[num]

def unionParent(arr, a, b):
    a = getParent(arr, a)
    b = getParent(arr, b)
    if a < b : arr[b] = a
    else: arr[a] = b

def isSameParent(arr, a, b):
    a = getParent(arr, a)
    b = getParent(arr, b)
    return True if a == b else False

n, m = map(int, input().split())
arr = list(range(n+1))
for _ in range(m):
    c, n1, n2 = map(int, input().split())

    if c == 0:
        unionParent(arr, n1, n2)
    elif c == 1:
        print('YES') if isSameParent(arr, n1, n2) else print('NO')