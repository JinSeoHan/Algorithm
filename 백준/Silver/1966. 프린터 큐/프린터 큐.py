import sys 
from collections import deque
input = sys.stdin.readline

testNum = int(input())
for _ in range(testNum):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while True:
        maxV = max(queue)
        front = queue.popleft()
        m -= 1

        if front == maxV:
            count += 1
            if m < 0:
                print(count)
                break;
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1