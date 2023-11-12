from collections import deque
def solution(storey):
    queue = deque()
    queue.append((list(str(storey)), 0))
    
    result = 1000000000
    while queue:
        v, cnt = queue.popleft()
        if len(v) == 1:
            result = min(result, cnt+int(v[0]), cnt + 10 - int(v[0]) + 1)
            continue

        e = int(v.pop())
        front = int(''.join(v))

        queue.append((v, cnt + e))
        v = list(str(front+1))
        queue.append((v, cnt + 10 - e))
    return result