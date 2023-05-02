n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())));
l.sort(key=lambda x: (x[1], x[0]))
for i in l:
    print(*i)