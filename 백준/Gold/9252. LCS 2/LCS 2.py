import sys
input = sys.stdin.readline

w1 = list(input().strip())
w2 = list(input().strip())

lcsMem = [0] * len(w1)
lenW1 = len(w1)
ord = [[] for i in range(lenW1)]
for c in w2:
    cnt = 0
    idx = 0
    for i in range(lenW1):
        if lcsMem[i] > cnt:
            cnt = lcsMem[i]
            idx = i
        elif w1[i] == c:
            lcsMem[i] = cnt + 1

            if ord[idx]:
                l = ord[idx].copy()
                l.append(c)
                ord[i] = l
            else:
                ord[i].append(c)

maxLen = 0
maxidx = 0
for i, v in enumerate(lcsMem):
    if v > maxLen:
        maxLen = v
        maxidx = i
print(maxLen)
print(''.join(ord[maxidx]))