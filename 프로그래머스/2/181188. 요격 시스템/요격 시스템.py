def solution(targets):
    targets.sort()
    
    endPoint = 0
    result = 0
    for target in targets:
        s, e = target[0], target[1]
        
        if endPoint > s:
            endPoint = min(endPoint, e)
        else:
            result += 1
            endPoint = e
    return result