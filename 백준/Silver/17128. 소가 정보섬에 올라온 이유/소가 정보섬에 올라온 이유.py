N, Q = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

fourMulList = []
for i in range(len(a)):
    val = list(map(lambda x : x  % len(a), [i, i+1, i+2, i+3]))
    fourMulList.append(a[val[0]]*a[val[1]]*a[val[2]]*a[val[3]])

s = sum(fourMulList)
for i in q:
    for x in range(i-4, i):
        fourMulList[x] *= -1
        s += 2*fourMulList[x]
    print(s)