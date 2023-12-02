from itertools import combinations
def solution(relation):
    result = 0
    row, col = len(relation), len(relation[0])
    
    #모든 속성 조합
    colPairs = []
    for i in range(1, col+1):
        colPairs.extend(combinations(range(col), i))
    
    #유일성 체크
    uniq = []
    for colPair in colPairs:
        table = [tuple([row[colIdx] for colIdx in colPair]) for row in relation]
        
        #유일성 체크
        flag = False
        if len(set(table)) == row:
            flag = True
            #최소성 체크
            for v in uniq:
                if v.issubset(set(colPair)): 
                    flag = False
                    break
        if flag:
            uniq.append(set(colPair))
                    
            
    return len(uniq)