x = int(input())
max = 0
i, j = 0, 0
while max < x:
    max = (1 + i)*i//2
    i += 1
if(i % 2 == 0):
    print(f'{1+(max-x)}/{i-1-(max-x)}')
else:
    print(f'{i-1-(max-x)}/{1+(max-x)}')