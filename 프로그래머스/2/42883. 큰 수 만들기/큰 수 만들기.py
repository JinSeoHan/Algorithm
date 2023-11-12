from collections import deque
def solution(number, k):
    number = deque(number)
    
    stack = []
    cnt = 0
    while number:
        num = number.popleft()
        #stack 비어있으면 채움
        if not stack:
            stack.append(num)
            continue
        #stack에 항상 큰 값이 담기도록 설정
        flag = False
        while stack and  stack[-1] < num:
            stack.pop()
            cnt += 1
            if cnt == k:
                flag = True
                break
        #스택을 채움
        stack.append(num)
        if flag: break
    #잔여개수 제거
    while stack and cnt != k:
        stack.pop()
        cnt += 1
    return ''.join(stack) + ''.join(number)