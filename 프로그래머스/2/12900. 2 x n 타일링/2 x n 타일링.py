def solution(n):
    l = [0, 1, 2]
    for i in range(3, n+1):
        l.append(l[-1]+l[-2])
        l[-1] %= 1000000007
    return l[-1]