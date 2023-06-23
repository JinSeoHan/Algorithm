import sys
input = sys.stdin.readline

s = []
s.append(input().rstrip())
s.append(input().rstrip())

s0Len = len(s[0])
s1Len = len(s[1])
l = [[0] * (s0Len+1) for i in range(s1Len+1)]
maximum = 0
for i in range(1, (s1Len + 1)):
    for j in range(1, (s0Len + 1)):
        if s[0][j-1] == s[1][i-1]:
            l[i][j] = l[i-1][j-1] + 1
        else:
            l[i][j] = max(l[i-1][j], l[i][j-1])
print(l[-1][-1])