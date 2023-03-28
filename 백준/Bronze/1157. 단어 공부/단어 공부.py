s = input().upper()
undu = list(set(s))
d = []
for u in undu:
    d.append(s.count(u))
print('?') if d.count(max(d)) > 1 else print(undu[d.index(max(d))])