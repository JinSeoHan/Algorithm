import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trainList = [0]*(n+1)

for _ in range(m):
    q = list(map(int, input().split()))
    match q[0]:
        case 1:
            trainList[q[1]] |= (1 << (q[2]-1))
        case 2:
            trainList[q[1]] &= ~(1 << (q[2]-1))
        case 3:
            trainList[q[1]] <<= 1
            trainList[q[1]] &= ((1 << 20)-1)
        case 4:
            trainList[q[1]] >>= 1

visited = [False]*(1<<20)
result = 0

for i in range(1, n+1):
    if not visited[trainList[i]]:
        result += 1
        visited[trainList[i]] = True
print(result)