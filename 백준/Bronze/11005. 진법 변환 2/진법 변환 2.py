N, B = map(int, input().split())
result = []
while N > 0:
    N, mod = divmod(N, B)
    result += [mod]
for i in range(len(result)):
    e = result.pop();
    if e > 9:
        print(chr(65+e-10), end='')
    else:
        print(str(e), end='')
