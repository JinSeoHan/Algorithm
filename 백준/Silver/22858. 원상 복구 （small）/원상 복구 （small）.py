import sys
input = sys.stdin.readline

n, k = map(int, input().split())

s = list(map(int, input().split()))
d = list(map(int, input().split()))

def shuffle(d, s):
    l = [0]*len(s)
    for i, v in enumerate(d,1):
        # i번째 카드를 v번째로 이동
        l[v-1] = s[i-1]
    return l
for i in range(k):
    s = shuffle(d, s)
print(*s)