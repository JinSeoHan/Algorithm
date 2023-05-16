import sys
input = sys.stdin.readline

n = int(input())

lArr = set()
for i in range(n):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        lArr.add(a)
        lArr.add(b)
        for j in range(i+1, n):
            a, b = input().split()
            if a in lArr:
                # print(f'a : {a}')
                lArr.add(b)
            elif b in lArr:
                # print(f'b : {b}')
                lArr.add(a)
        break
print(len(lArr))