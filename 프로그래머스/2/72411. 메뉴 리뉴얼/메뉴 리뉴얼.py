from itertools import combinations
from collections import Counter
def solution(orders, course):

    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        count = Counter(temp)
        
        if not count or max(count.values()) == 1: continue
        for k, v in count.items():
            if v == max(count.values()):
                answer.append(''.join(k))
    return sorted(answer)
            