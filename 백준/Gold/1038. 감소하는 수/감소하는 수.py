import sys
input = sys.stdin.readline

n = int(input())

if n < 10:
    print(n)
    exit(0)
memo = [[] for row in range(10)]
memo[0].extend(['0','1','2','3','4','5','6','7','8','9'])

cnt = 9
for sTop in range(1, 10):
    for top in range(sTop, 10):
        for v in memo[sTop-1]:
            if top > int(v[0]):
                memo[sTop].append(str(top) + v)
                cnt += 1

                if cnt == n:
                    print(memo[sTop][-1])
                    exit(0)
print(-1)