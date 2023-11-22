def newTime(book_time):
    for i in range(len(book_time)):
        l = book_time[i]
        h, m = map(int, l[0].split(':'))
        l[0] = h*60+m
        h, m = map(int, l[1].split(':'))
        l[1] = h*60+m
    return book_time
        
        
        
def solution(book_time):
    #겹치는 시간의 개수의 최대값을 찾는 문제
    result = 0
    book_time = newTime(book_time)
    book_time.sort(reverse=True)
    
    rooms = []
    while book_time:
        curTime = book_time.pop()
        
        if len(rooms) == 0:
            rooms.append([curTime])
            continue
            
        isInsert = None
        #방을 선택
        for room in rooms:
            isInsert = True
            #방에 저장된 시간
            for time in room:
                #겹치는 시간이 있는지 검사
                if time[0] <= curTime[0] < time[1]+10:
                    isInsert = False
                    break
            if not isInsert: continue
            room.append(curTime)
            break
        if not isInsert:
            rooms.append([curTime])
    return len(rooms)
            
                    
            
            