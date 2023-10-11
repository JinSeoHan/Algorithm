from collections import defaultdict
def solution(dirs):
    visited = defaultdict(int)
    x, y = 5, 5
    cnt = 0
    for dir in dirs:
        if dir == 'U':
            if not isValid(x, y + 1):
                continue
            if visited[(x,y,x,y+1)] == 0:
                visited[(x,y,x,y+1)] = True
                visited[(x,y+1,x,y)] = True
                cnt += 1
            y += 1
        elif dir == 'D':
            if not isValid(x, y - 1):
                continue
            if visited[(x,y,x,y-1)] == 0:
                visited[(x,y,x,y-1)] = True
                visited[(x,y-1,x,y)] = True
                cnt += 1
            y -= 1
        elif dir == 'R':
            if not isValid(x + 1, y):
                continue
            if visited[(x,y,x+1,y)] == 0:
                visited[(x,y,x+1,y)] = True
                visited[(x+1,y,x,y)] = True
                cnt += 1
            x += 1
        elif dir == 'L':
            if not isValid(x - 1, y):
                continue
            if visited[(x,y,x-1,y)] == 0:
                visited[(x,y,x-1,y)] = True
                visited[(x-1,y,x,y)] = True
                cnt += 1
            x -= 1
    return cnt 
def isValid(x, y):
    return 0 <= x <= 10 and 0 <= y <= 10