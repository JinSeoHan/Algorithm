import heapq
def solution(n, k, enemy):
    
    heap = []
    sum = 0
    result = 0
    for i, v in enumerate(enemy):
        heapq.heappush(heap, v)
        
        if len(heap) > k:
            n -= heapq.heappop(heap)
        if n < 0:
            return i
            
        
    return len(enemy)