def solution(m, musicinfos):
    m = list(m)
    for i in range(len(m)):
        if m[i] == '#':
            m[i-1] += m[i]
    while '#' in m:
        m.remove('#')
    
    result = []
    for info in musicinfos:
        sTime,eTime,title,ord = info.split(',')
        sh, sm = map(int, sTime.split(':'))
        eh, em = map(int, eTime.split(':'))
        
        #ord 추출
        ord = list(ord)
        for i in range(len(ord)):
            if ord[i] == '#':
                ord[i-1] += ord[i]
        while '#' in ord:
            ord.remove('#')

        #분으로 변환
        minTime = (eh-sh)*60-sm+em
        
        #출력된 음악의 악보를 저장
        music = []
        for i in range(minTime):
            music.append(ord[i%len(ord)])
        #악보속 멜로디가 있는지 확인
        for i in range(len(music)):
            if music[i] == m[0] and i+len(m) <= len(music):
                if m == music[i:i+len(m)]:
                    result.append((minTime, title))
                    break
    result.sort(reverse=True, key=lambda x : x[0])
    if len(result) == 0:
        return "(None)"
    else:
        return result[0][1]
