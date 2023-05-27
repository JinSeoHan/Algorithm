import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    try:
        p = input().rstrip()
        n = int(input())
        isLeft = True

        #문자열 가공 후 deque에 넣기
        arr = input().rstrip().lstrip('[').rstrip(']').split(',')
        if arr[0] == '':
            del arr[0]
        qArr = deque(arr)

        for i in p:
            if i == 'R':
                isLeft = not isLeft
            elif i == 'D':
                if isLeft:
                    qArr.popleft()
                else:
                    qArr.pop()
        print('[', end='')
        if len(qArr) != 0:
            if isLeft:
                print(qArr.popleft(), end='')
                for i in qArr:
                    print(f',{i}', end='')
            else:
                print(qArr.pop(), end='')
                while qArr:
                    print(f',{qArr.pop()}', end='')
        print(']')
    except :
        print('error')