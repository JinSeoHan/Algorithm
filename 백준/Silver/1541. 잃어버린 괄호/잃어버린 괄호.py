import sys
input = sys.stdin.readline

s = input()
p = [0]
m = [0]

idx = s.find('-')
if idx != -1:
    left = s[:idx]
    right = s[idx+1:]
    p = list(map(int, left.split('+')))
    m = list(map(int, right.replace('-', '+').split("+")))
else:
    p = list(map(int, s.split('+')))
print(sum(p)-sum(m))