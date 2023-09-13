from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    while progresses and speeds:
        #progresses삭제 로직 
        flag = False
        cnt = 0
        while progresses and progresses[0] > 99:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            flag = True
        if flag: answer.append(cnt)
        if not progresses: break
        #progresses전체를 speed만큼 올리는 로직
        for i, v in enumerate(progresses):
            progresses[i] += speeds[i]
    return answer