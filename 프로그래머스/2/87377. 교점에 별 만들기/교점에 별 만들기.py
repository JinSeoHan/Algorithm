from itertools import combinations
def getBoardRange(starCoords):
    sx,sy, ex,ey = 1000000000000000, - 1000000000000000, -1000000000000000, 1000000000000000
    for coord in starCoords:
        sx = min(sx, coord[0])
        sy = max(sy, coord[1])
        ex = max(ex, coord[0])
        ey = min(ey, coord[1])
    return sx, sy, ex, ey
def getCrossCoord(A,B,E,C,D,F):
    if A*D-B*C == 0: return None, None
    return (B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C)
def solution(line):
    answer = []
    starCoords = set()#별좌표 저장
    #모든 직선의 교점 찾기
    for l in combinations(line, 2):
        A, B, E = l[0]
        C, D, F = l[1]
        
        #두 직선의 교점을 찾음
        x, y = getCrossCoord(A,B,E,C,D,F)
        
        #두 직선의 교점이 평행 또는 일치할 경우
        if x == y == None or not x.is_integer() or not y.is_integer(): continue
        
        #별 좌표를 저장함
        starCoords.add((int(x),int(y)))
    #별 그리기
    sx, sy, ex, ey = getBoardRange(starCoords)
    for y in range(sy, ey-1, -1):
        answer.append([])
        for x in range(sx, ex+1):
            if (x,y) in starCoords:
                answer[-1].append('*')
            else:
                answer[-1].append('.')
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer