import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def divisoin(il, ir, pl, pr):
    if not (il <= ir and pl <= pr):
        return
    
    root = postOrder[pr]
    print(root, end=' ')

    inorderRootIdx = inorderIdx[root]

    left = inorderRootIdx - il
    right = ir - inorderRootIdx
    divisoin(il, il+left-1, pl,pl+left-1)
    divisoin(ir-right+1, ir, pr-right, pr-1)

n = int(input())
inorder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

#inorder의 위치값 저장
inorderIdx = dict()
for i, v in enumerate(inorder):
    inorderIdx[v] = i

pre = []
divisoin(0, n-1, 0, n-1)