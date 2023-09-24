def solution(msg):
    l = ['']
    for i in range(ord('A'), ord('Z')+1):
        l.append(chr(i))
        
    answer = []
    wc = ''
    prev = ''
    for m in msg:
        wc += m
        if wc not in l:
            l.append(wc)
            answer.append(l.index(prev))
            wc = wc[-1]
        prev = wc
    answer.append(l.index(prev))
    return answer