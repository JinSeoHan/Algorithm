from collections import Counter
def getParent(parent, a):
    if parent[a] == a: return a
    parent[a] = getParent(parent, parent[a])
    return parent[a]
def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a > b: 
        parent[a] = b
    else:
        parent[b] = a
    
def solution(cards):
    parent = [i for i in range(len(cards)+1)]
    
    for i, card in enumerate(cards, 1):
        union(parent, i, card)
    
    for card in cards:
        getParent(parent, card)
    parent = parent[1:]
    count = list(Counter(parent).values())
    count.sort()
    if len(count) == 1:
        return 0
    return count[-1] * count[-2]