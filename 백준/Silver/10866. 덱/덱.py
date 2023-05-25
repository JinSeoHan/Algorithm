from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
for i in range(int(input())):
    cmd = input().rstrip('\n')

    if len(queue) == 0 and (cmd == 'empty' or cmd == 'front' or cmd == 'back' or cmd == 'pop_front' or cmd == 'pop_back'):
        if cmd == 'empty':
            print(1)
        else:
            print(-1)
        continue
    if cmd == 'front':
        print(queue[0])
        continue
    elif cmd == 'back':
        print(queue[-1])
        continue
    elif cmd == 'size':
        print(len(queue))
        continue
    elif cmd == 'empty':
        print(0)
        continue
    elif cmd == 'pop_back':
        print(queue.pop())
        continue
    elif cmd == 'pop_front':
        print(queue.popleft())
        continue
    
    cmd, v = cmd.split()
    if cmd == 'push_back':
        queue.append(v)
    elif cmd == 'push_front':
        queue.appendleft(v)