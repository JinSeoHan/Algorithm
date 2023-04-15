n = int(input())
m = 0
result = 0
while m < n:
    arr = list(map(int, str(m)))
    if sum(arr) + int(m) == n:
        print(m)
        exit()
    m += 1 
print(result)