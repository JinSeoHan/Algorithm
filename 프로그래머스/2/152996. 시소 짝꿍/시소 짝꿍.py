from collections import Counter
def solution(weights):
    counter = Counter(weights)
    result = 0
    for k, v in counter.items():
        if v >= 2:
            result += v*(v-1)//2
    
    for k, v in counter.items():
        for a in (3/2, 2, 4/3):
            if k * a in counter.keys():
                result += counter[k] * counter[k*a]
    return result