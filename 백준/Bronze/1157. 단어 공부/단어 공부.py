a = input().upper()
d = {}
for s in a:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
temp = [k for k, v in d.items() if v == max(d.values())]
print(*temp) if len(temp) == 1 else print('?')