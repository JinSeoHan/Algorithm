from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    
    s = set()
    if x == y: return 0
    while queue:
        num, cnt = queue.popleft()
        if num in s: continue
        s.add(num)
        for v in (num+n, num*2, num*3):
            if v == y:
                return cnt + 1
            if v < y:
                queue.append((v, cnt+1))
    return -1