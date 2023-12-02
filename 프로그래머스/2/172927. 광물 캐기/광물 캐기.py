def solution(picks, minerals):
    newM = [[0,0,0] for row in range(10)]
    #캘 수 있는 광물의 개수를 구함
    s = sum(picks) * 5
    if s < len(minerals):
        minerals = minerals[:s]
        
    #5개씩 잘라서 담음
    idx1, idx2 = 0, 0
    while idx1 < len(minerals):
        if idx1 != 0 and idx1 % 5 == 0:
            idx2 += 1
        if minerals[idx1] == 'diamond':
            newM[idx2][0] += 1
        elif minerals[idx1] == 'iron':
            newM[idx2][1] += 1
        elif minerals[idx1] == 'stone':
            newM[idx2][2] += 1
        idx1 += 1
    #피로도가 높은 순으로 정렬
    newM.sort(key=lambda x : (-x[0], -x[1], -x[2]))
        
    
    #피로도 계산
    result = 0
    for d, i, s in newM:
        for pickNum in range(len(picks)):
            if pickNum == 0 and picks[pickNum] > 0:#다이아곡괭이
                picks[pickNum] -= 1
                result += d + i + s
                break
                
            elif pickNum == 1 and picks[pickNum] > 0:#철곡괭이
                picks[pickNum] -= 1
                result += 5*d + i + s
                break
            elif pickNum == 2 and picks[pickNum] > 0:#돌곡괭이
                picks[pickNum] -= 1
                result += 25*d + 5*i + s
                break
                
    return result