from collections import defaultdict, Counter
def solution(topping):
    a = Counter(topping)
    b = defaultdict(int)
    
    cnt = 0
    for i in range(len(topping)):
        v = topping[i]
        b[v] += 1
        a[v] -= 1
        
        if a[v] == 0:
            del a[v]
        if len(a) == len(b):
            cnt += 1
    return cnt