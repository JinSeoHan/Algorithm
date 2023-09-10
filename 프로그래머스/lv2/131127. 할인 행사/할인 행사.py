def solution(want, number, discount):
    discountDict = dict()
    l,r = 0, 0
    cnt = 0
    for i in range(10):
        if discount[r] not in discountDict:
            discountDict[discount[r]] = 1
        else:
            discountDict[discount[r]] += 1
        r += 1
        
    if isPosible(discountDict, want, number):
        cnt += 1
    while r < len(discount):
        if discount[r] not in discountDict:
            discountDict[discount[r]] = 1
        else:
            discountDict[discount[r]] += 1
        discountDict[discount[l]] -= 1
        
        if isPosible(discountDict, want, number):
            cnt += 1
            
        r += 1
        l += 1
        
    return cnt
def isPosible(discountDict, want, number):
    for idx, number in enumerate(number):
        if want[idx] not in discountDict or discountDict[want[idx]] != number: return False
    return True