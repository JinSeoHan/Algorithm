a, b = map(int, input().split())
result = []

for i in range(1, a + 1):
    if a % i == 0:
        result.append(i)
if len(result) < b:
    print(0)
else: 
    print(result[b-1])