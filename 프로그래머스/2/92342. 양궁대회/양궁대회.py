from itertools import combinations_with_replacement
def solution(n, info):
    result = [-1]
    
    #중복조합으로 과녁0~10사이의 수 n개를 뽑는다.
    mscore = 0
    mxDiff = -1
    for combi in combinations_with_replacement(range(11), n):
        #라이언 점수표
        linfo = [0] * 11
        #뽑은 과녁리스트의 값 기준으로 개수를 셈
        for i in combi:
            linfo[10-i] += 1
            
        #어피치와 라이언의 점수를 구함
        ascore, lscore = 0, 0
        for i in range(11):
            if info[i] == linfo[i] == 0: continue
            if linfo[i] > info[i]:
                lscore += 10 - i
            else:
                ascore += 10 - i
        if lscore > ascore:
            diff = lscore - ascore
            if mxDiff < diff:
                mxDiff = diff
                result = linfo
    return result
        
        