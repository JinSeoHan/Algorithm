def solution(n):
    sum = 0
    result = 0
    l, r = 0, 0
    while r <= n:
        if sum < n:
            r += 1 
            sum += r
        else:
            l += 1
            sum -= l
        if sum == n:
            result += 1
    return result