n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)
result = 0
while l:
    result = max(result, len(l)*l.pop())
print(result)