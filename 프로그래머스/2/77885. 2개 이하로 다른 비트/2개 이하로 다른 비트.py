def solution(numbers):
    result = []
    for i in numbers:
        result.append(f(i))
    return result
def f(num):
    if bin(num)[-1] == '0':
        return num+1
    n = num + 1
    n = num ^ n
    n >>= 1
    n += 1
    n >>= 1
    return num + n