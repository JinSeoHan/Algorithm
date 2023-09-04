import heapq
def solution(people, limit):
    people.sort()
    cnt = 0
    l, r = 0, len(people)-1
    while l <= r:
        sum = people[l] + people[r]
        if sum > limit:
            r -= 1
            cnt += 1
        elif sum <= limit:
            l += 1
            r -= 1
            cnt += 1
    return cnt
