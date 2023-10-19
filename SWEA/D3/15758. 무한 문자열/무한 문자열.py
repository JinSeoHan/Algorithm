T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    
    a, b = input().split()
    
    flag = True
    while len(a) and len(b):
        #a에 긴 문자열 세팅
        if len(a) < len(b) : 
            a, b = b, a
        if b not in a:
            flag = False
            break
        while b in a:
            a = a.replace(b, '')
    
    print('yes') if flag else print('no')