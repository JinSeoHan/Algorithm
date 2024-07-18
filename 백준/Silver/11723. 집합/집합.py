import sys
input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    q = input()
    cmd = q.split()
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
    if cmd[0] == 'add':
        s.add(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in s:
            s.remove(cmd[1])
    elif cmd[0] == 'check':
        print(1) if cmd[1] in s else print(0)
        
    elif cmd[0] == 'toggle':
        s.remove(cmd[1]) if cmd[1] in s else s.add(cmd[1])
    elif cmd[0] == 'all':
        s = set(range(1, 21))
    elif cmd[0] == 'empty':
        s = set()