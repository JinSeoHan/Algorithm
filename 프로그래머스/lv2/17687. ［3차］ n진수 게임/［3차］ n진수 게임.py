def solution(n, t, m, p):
    
    gameNum = '0'
    
    for i in range(t*m):
        gameNum += ''.join(convert(i,n))
    
    result = ''
    cnt = 0
    cnt2 = 0
    for i in range(1, len(gameNum)+1):
        if cnt2 == t: break
        if cnt % m == p-1:
            result += gameNum[cnt]
            cnt2 += 1
        cnt += 1
        
    return result
def convert(num, n):
    numbers = list(map(str, range(10)))
    numbers.extend(['A', 'B', 'C', 'D', 'E', 'F'])
    result = []
    while num:
        result.append(numbers[num%n])
        num //= n
    result.reverse()
    return result
    