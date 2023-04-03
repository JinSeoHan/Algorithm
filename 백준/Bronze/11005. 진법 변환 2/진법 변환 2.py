N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while N > 0:
    N, mod = divmod(N, B)
    result += number[mod]
print(result[::-1])