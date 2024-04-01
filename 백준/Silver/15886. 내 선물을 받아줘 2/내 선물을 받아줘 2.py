n = int(input())
q = input()
result = 0
for i, v in enumerate(q):
    if i != 0 and v == 'W' and q[i-1] == 'E':
        result += 1
    elif i == 0 and v == 'W':
        result += 1
    elif i == len(q)-1 and v == 'E':
        result += 1
print(result)