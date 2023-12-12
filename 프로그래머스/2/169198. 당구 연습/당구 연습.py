def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        temp = []
        #위벽
        if not (ball[0] == startX and ball[1] > startY):
            d = (ball[0] - startX)**2 + (ball[1] - 2*n + startY)**2
            temp.append(d)
        #아래벽
        if not (ball[0] == startX and ball[1] < startY):
            d = (ball[0] - startX)**2 + (ball[1] + startY)**2
            temp.append(d)
        #우벽
        if not (ball[0] > startX and ball[1] == startY):
            d = (ball[0] - 2*m + startX)**2 + (ball[1] - startY)**2
            temp.append(d)
        #좌벽
        if not (ball[0] < startX and ball[1] == startY):
            d = (ball[0] + startX)**2 + (ball[1] - startY)**2
            temp.append(d)
        
        answer.append(min(temp))
    return answer