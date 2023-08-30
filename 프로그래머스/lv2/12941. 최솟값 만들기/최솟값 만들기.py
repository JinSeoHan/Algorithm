import heapq

def solution(A,B):
    heapq.heapify(A)
    heapB = []
    for i in B:
        heapq.heappush(heapB, -i)
    sum = 0
    while A and heapB:
        sum += heapq.heappop(A) * -heapq.heappop(heapB)
    return sum