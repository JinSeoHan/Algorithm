import heapq
def solution(N, road, K):
    #그래프 정보 저장
    graph = [[] for v in range(N+1)]
    
    for info in road:
        s, d, e = info[0], info[1], info[2]
        graph[s].append((e, d))
        graph[d].append((e, s))
    
    #1번 출발 도착 최단거리
    INF = 100000000000
    dist = [INF] *(N+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        cc, cv = heapq.heappop(heap)
        for nc, nv in graph[cv]:
            if cc+nc < dist[nv]:
                dist[nv] = cc+nc
                heapq.heappush(heap, (dist[nv], nv))

    cnt = 0
    for i in dist:
        if i <=K:
            cnt += 1
    return cnt