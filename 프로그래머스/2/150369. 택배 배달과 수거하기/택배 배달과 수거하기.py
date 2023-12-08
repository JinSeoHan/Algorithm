def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    deliveryCnt, pickupCnt = 0, 0
    for i in range(n):
        deliveryCnt += deliveries[i]
        pickupCnt += pickups[i]
        
        while deliveryCnt > 0 or pickupCnt > 0:
            deliveryCnt -= cap
            pickupCnt -= cap
            answer += (n-i)*2
    
    return answer