from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    
    dic = defaultdict(list)
    for i in info:
        information = i.split()
        key = information[:-1]
        score = int(information[-1])
        for j in range(5):
            for combi in combinations([0,1,2,3], j):
                tmp = key.copy()
                for c in combi:
                    tmp[c] = '-'
                dic[''.join(tmp)].append(score)
    for v in dic.values():
        v.sort()
    
    for q in query:
        q = q.replace('and ', '')
        q = q.split()
        key = ''.join(q[:-1])
        score = int(q[-1])
        
        count = 0
        if key in dic:
            scores = dic[key]
            idx = bisect_left(scores, score)
            count = len(scores) - idx
        
        answer.append(count)
    return answer