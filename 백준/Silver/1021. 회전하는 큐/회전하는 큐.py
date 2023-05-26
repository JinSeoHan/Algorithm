from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
printQueue = deque(list(map(int, input().split())))

count = 0
while printQueue:
    target = printQueue.popleft()
    currPosition = queue.index(target)

    mid = len(queue) // 2
    if currPosition <= mid:
        for _ in range(currPosition):
            queue.append(queue.popleft())
            count += 1
        queue.popleft()
    else:
        for _ in range(len(queue) - currPosition):
            queue.appendleft(queue.pop())
            count += 1
        queue.popleft()
print(count)