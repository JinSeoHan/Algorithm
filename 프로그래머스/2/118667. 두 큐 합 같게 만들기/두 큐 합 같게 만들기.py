from collections import deque
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    
    cnt = 0
    for i in range(len(queue1) * 3):
        if s1 == s2:
            return cnt
        
        if s1 > s2:
            v = q1.popleft()
            s1 -= v
            s2 += v
            q2.append(v)
            cnt += 1
        elif s1 < s2:
            v = q2.popleft()
            s2 -= v
            s1 += v
            q1.append(v)
            cnt += 1
        
    return -1