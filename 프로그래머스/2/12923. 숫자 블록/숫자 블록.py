def getV(num):
    stack = [1]
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if num//i > 10000000:
                stack.append(i)
                continue
            return num//i
    return max(stack)
def solution(begin, end):
    result = []
    for i in range(begin, end+1):
        if i == 1: result.append(0)
        elif i < 4: result.append(1)
        else: result.append(getV(i))
    return result