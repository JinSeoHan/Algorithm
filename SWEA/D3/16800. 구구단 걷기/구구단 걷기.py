from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    a = int(input())
    
    for i in range(int(a**(0.5)), 0, -1):
        if a % i == 0:
            n1 = a // i
            n2 = i
            print(a//i+i-2)
            break