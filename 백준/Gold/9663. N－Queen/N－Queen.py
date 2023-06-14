import sys
input = sys.stdin.readline

def queen(d):
    global count

    if d == n:
        count += 1
        return

    for i in range(n):
        if isPoss(d, i):
            queenPos[d] = i
            queen(d + 1)
            queenPos[d] = -1
            
def isPoss(d, c):
    for i in range(d):
        if queenPos[i] == c or (d - i) == abs(queenPos[i]-c):
            return False

    return True

n = int(input())
queenPos = [-1] * n
count = 0
queen(0)
print(count)