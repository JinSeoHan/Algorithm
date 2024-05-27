import sys
input = sys.stdin.readline

k = int(input())
q = list(map(int, input().split(' ')))
depth = [[] for i in range(k+1)]
def recursion(s,e,d):
    global depth
    if d > k: return
    mid = (s+e)//2
    depth[d].append(str(q[mid]))
    recursion(s,mid-1,d+1)
    recursion(mid+1,e,d+1)

recursion(0,2**k-2,1)
for i in range(1, k+1):
    print(' '.join(depth[i]))