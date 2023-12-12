def f(n, k):
    if n == 1:
        return k if k <= 2 else k-1
    
    unit = 5**(n-1)#n-1비트열의 비트수
    oneCnt = 4**(n-1)#n-1비트열 1개수
    location = k//unit#n비트열 위치번호 0 1 2 3 4
    
    #k가 5의 배수라면 비트열 위치를 한 칸 감소
    if k % unit == 0:
        location -= 1
    
    if location < 2:
        return location*oneCnt + f(n-1, k-unit*location)
    elif location == 2:
        return oneCnt*(location)
    else:
        return (location-1)*oneCnt + f(n-1, k-unit*location)
        
    
def solution(n, l, r):
    #n비트열에서 r까지의 1개수 - (l-1)까지의 1개수
    return f(n, r) - f(n, l-1)