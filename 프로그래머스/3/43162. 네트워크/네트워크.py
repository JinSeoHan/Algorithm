def solution(n, computers):
    parent = list(range(n))
    for i, v in enumerate(computers):
        for j, v2 in enumerate(v):
            if v2:
                union(parent, i, j)
    result = set()
    for i in range(n):
        result.add(getParent(parent, i))
    return len(result)

def getParent(parent, a):
    if parent[a] == a : return a
    parent[a] = getParent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    
    if a < b: parent[b] = a
    else: parent[a] = b