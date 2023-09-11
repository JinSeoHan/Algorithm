from collections import deque
def solution(cacheSize, cities):
    queue = deque()
    answer = 0
    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            if cacheSize > 0 : queue.append(city)
            answer += 1
            continue
        if len(queue) < cacheSize:
            if cacheSize > 0: queue.append(city)
            answer += 5
            continue
        if city not in queue:
            if queue: queue.popleft()
            if cacheSize > 0: queue.append(city)
            answer += 5
    return answer