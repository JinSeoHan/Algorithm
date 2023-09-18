def solution(n, k):
    #진법변환
    strNums = ''
    while n != 0:
        strNums = str(n%k) + strNums
        n //= k
    #1000000이하의 소수를 찾음
    prime = [True]*1000001
    prime[0], prime[1] = False, False
    for i in range(2, int(1000001**0.5)):
        if not prime[i]: continue
        cnt = 2
        value = i * cnt
        while value <= 1000000:
            prime[value] = False
            cnt += 1
            value = i * cnt
    result = 0
    l = list(strNums.split('0'))
    for number in l:
        if number != '' and int(number) >= 2:
            number = int(number)
            isPrime = True
            for i in range(2, int(number**0.5)+1):
                if number % i == 0: 
                    isPrime = False
                    break
            if isPrime:
                result += 1
    return result