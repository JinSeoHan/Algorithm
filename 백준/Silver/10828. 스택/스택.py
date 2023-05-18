import sys
input = sys.stdin.readline

n = int(input())

lArr = list()
for _ in range(n):
    command = input().rstrip()

    if ' ' in command:
        c, v = command.split()
        lArr.append(v)
    else:
        if command == 'pop':
            if len(lArr) == 0:
                print(-1)
            else:
                print(lArr.pop())
        elif command == 'size':
            print(len(lArr))
        elif command == 'empty':
            if len(lArr) == 0:
                print(1)
            else:
                print(0)
        elif command == 'top':
            if len(lArr) == 0:
                print(-1)
            else:
                print(lArr[-1])