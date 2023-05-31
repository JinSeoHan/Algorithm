import sys
input = sys.stdin.readline

def removeMiddle(l : list):
    if len(l) == 1:
        return l

    spaceCount = len(l) // 3
    leftL = removeMiddle(l[:spaceCount])
    rightL = removeMiddle(l[spaceCount*2:])
    return leftL + [' ']*spaceCount + rightL


n = input().rstrip()
if n == '': 
    exit(0)
n = int(n)
while True:
    try:
        n = 3 ** n
        l = ['-']*n
        l = removeMiddle(l)
        print(''.join(l))
        n = int(input())
    except:
        break