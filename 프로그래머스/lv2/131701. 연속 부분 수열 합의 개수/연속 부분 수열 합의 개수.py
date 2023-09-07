def solution(elements):
    n = len(elements)
    result = set()
    
    for i in range(1, n+1):
        l, r = n, n
        total = 0
        while r > 0:
            if r - l < i:
                l -= 1
                total += elements[l]
            else:
                l, r = l-1, r-1
                total += elements[l]
                total -= elements[r]
            result.add(total)
    return len(result)