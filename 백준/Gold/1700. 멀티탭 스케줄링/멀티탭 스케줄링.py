import sys
from collections import Counter, deque
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
l = deque(map(int, input().split()))
count = Counter(l)

tap = [None]*n

minV = []
result = 0
for i in range(len(l)):
    #멀티탭에 이미 꽂혀있는 경우
    if l[i] in tap: continue
    #멀티탭에 빈곳이 있는 경우
    if None in tap:
        idx = tap.index(None)
        tap[idx] = l[i]
        continue
    #멀티탭에 하나를 뽑고 꽂아야하는 경우
    tidx = 0#뽑을 위치
    beforePrio = -1#우선순위
    for j in range(len(tap)):
        priority = 0#우선순위는 높을수록 좋음 / 멀티탭에 꽂혀있는 플러그중 가장 나중에 사용될 플러그위치를 찾음
        for k in range(i+1, len(l)):
            if tap[j] == l[k]:
                break
            priority += 1
        if priority > beforePrio:
            beforePrio = priority
            tidx = j
    tap[tidx] = l[i]
    result += 1
print(result)