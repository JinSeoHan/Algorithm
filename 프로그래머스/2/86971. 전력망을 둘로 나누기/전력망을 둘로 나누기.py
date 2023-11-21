from collections import defaultdict
def solution(n, wires):
    parent = [i for i in range(n+1)]
    def getParent(a):
        if parent[a] == a:
            return parent[a]
        parent[a] = getParent(parent[a])
        return parent[a]
    def union(a, b):
        a = getParent(a)
        b = getParent(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    answer = 1000000
    for wire in wires:
        parent = [i for i in range(n+1)]
        for w in wires:
            if wire == w : 
                continue
            union(w[0], w[1])
        
        #union 개수를 셈
        d = defaultdict(int)
        for i in range(1, n+1):
            d[getParent(i)] += 1
        temp = list(d.values())
        s = abs(temp[0] - temp[1])
        answer = min(answer, s)
            
    return answer