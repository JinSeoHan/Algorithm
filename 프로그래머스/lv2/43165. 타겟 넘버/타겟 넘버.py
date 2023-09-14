def solution(numbers, target):
    answer = 0
    DFS(0, 0, numbers, target)
    return cnt

cnt = 0
def DFS(idx, sum, numbers, target):
    global cnt
    if idx == len(numbers): 
        if sum == target:
            cnt += 1
        return
    for i in (1, -1):
        DFS(idx+1, sum+(i*numbers[idx]), numbers, target)