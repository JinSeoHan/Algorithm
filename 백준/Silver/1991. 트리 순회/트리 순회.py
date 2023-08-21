import sys
input = sys.stdin.readline

n = int(input())

edge = dict()

postV = dict()
for i in range(n):
    p, c1, c2 = input().split()
    postV[p] = False
    edge[p] = [c1]
    edge[p].append(c2)

def preorder(s):
    print(s, end='')
    if edge[s][0] != '.':
        preorder(edge[s][0])
    if edge[s][1] != '.':
        preorder(edge[s][1])
def inorder(s):
    if edge[s][0] != '.':
        inorder(edge[s][0])
    print(s, end='')
    if edge[s][1] != '.':
        inorder(edge[s][1])
def postorder(s):
    if edge[s][0] != '.':
        postorder(edge[s][0])
    if edge[s][1] != '.':
        postorder(edge[s][1])
    print(s, end='')
    
preorder('A')
print()
inorder('A')
print()
postorder('A')