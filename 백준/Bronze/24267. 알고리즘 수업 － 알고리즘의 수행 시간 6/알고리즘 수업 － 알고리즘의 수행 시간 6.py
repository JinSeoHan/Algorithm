n = int(input())
sum = 0
for k in range(2, n):
    sum += (n-k)*(n-k+1)//2
print(f'{sum}\n3')