from collections import deque
def solution(order):
    order = deque(order)
    answer = 0
    stack = []
    for i in range(1, len(order)+1):
        if stack and stack[-1] > i:
            break
        if i == order[0]:
            order.popleft()
            answer += 1
        else:
            stack.append(i)
        while stack and order and stack[-1] == order[0]:
            order.popleft()
            stack.pop()
            answer += 1
    return answer