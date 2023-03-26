i = int(input())
for a in range(1,2*i,2):
    print(' ' * (i-(a+1)//2), end='')
    print(('*' * a))
for a in range(2*i-3,0,-2):
    print(' ' * (i-(a+1)//2), end='')
    print(('*' * a))