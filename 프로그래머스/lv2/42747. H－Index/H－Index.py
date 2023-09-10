def solution(citations):
    citations.sort()
    
    totalCnt = len(citations)
    
    answer = 0
    for i in range(1, totalCnt+1):
        aNum = 0#i편이상 인용된 논문의 개수
        bNum = 0#i편이하 인용된 논문의 개수
        
        for j in citations:
            if j >= i:
                aNum += 1
            elif j <= i:
                bNum += 1
        if aNum >= i and bNum <= i:
            answer = i
    return answer