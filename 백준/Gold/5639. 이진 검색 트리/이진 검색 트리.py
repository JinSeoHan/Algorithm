import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []
while True:
    try:
        v = int(input())
        arr.append(v) 
    except:
        break

def post(l, r):
    if l > r:
        return
    root = arr[l]
    
    mid = r + 1
    for i in range(l+1, r+1):
        if root < arr[i]:
            mid = i
            break
    
    post(l+1, mid-1)
    post(mid, r)
    print(root)

post(0, len(arr)-1)