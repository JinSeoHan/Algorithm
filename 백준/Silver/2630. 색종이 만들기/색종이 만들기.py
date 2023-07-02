import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

w = 0
b = 0
def paper(r, c, len):
    global w, b
    color = l[r][c]
    for i in range(r, r+len):
        for j in range(c, c+len):
            if l[i][j] != color:
                paper(r, c, len//2)
                paper(r, c+len//2, len//2)
                paper(r+len//2, c, len//2)
                paper(r+len//2, c+len//2, len//2)
                return
    if color == 1:
        b += 1
    else:
        w += 1

paper(0, 0, n)
print(w)
print(b)