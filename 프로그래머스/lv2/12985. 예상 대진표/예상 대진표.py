from collections import deque
def solution(n,a,b):
    a, b = min(a, b), max(a, b)
    
    l = deque()
    for i in range(1, n+1):
        l.append((i,1))
        
    depth1, depth2 = 0, 0
    win = None
    while len(l) != 1:
        one, depth1 = l.popleft()
        two, depth2 = l.popleft()
        
        if one in [a,b] and two in [a,b]:
            break
        elif one in [a,b]:
            l.append((one, depth1+1))
        elif two in [a,b]:
            l.append((two, depth1+1))
        else:
            l.append((one, depth1+1))
        
    return depth1