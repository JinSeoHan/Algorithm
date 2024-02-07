import sys
input = sys.stdin.readline

q = input()
token = q.split()
# 변수가 없는 경우
if len(token) == 1:
    print(*token)
    exit(0)
# 변수가 존재하는 경우
common = token[0] # 공통타입
valList = list(map(lambda x : x[:-1],token[1:]))

for val in valList:
    result = common

    val = list(val)
    while len(val) > 1:
        e = val[-1]
        if e in ['&', '*']:
            result += e
        elif e == ']':
            val.pop()
            result += '[]'
        else:
            break
        val.pop()
    print(f'{result} {"".join(val)};')