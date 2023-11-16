def solution(n):
    mok = n
    v = ['1', '2', '4']
    result = ''
    while mok:
        if mok % 3 == 0:
            result += '4'
            mok = mok // 3 -1
        else:
            result += str(mok % 3)
            mok //= 3
    return result[::-1]