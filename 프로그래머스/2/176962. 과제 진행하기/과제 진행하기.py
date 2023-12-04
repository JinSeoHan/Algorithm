from collections import deque
def solution(plans):

    for i, plan in enumerate(plans):
        name, start, playtime = plan
        
        h, m = map(int, start.split(':'))
        plans[i][1] = h*60+m
        plans[i][2] = int(playtime)
    plans.sort(key=lambda x : x[1])

    stack = []
    result = []
    for idx in range(len(plans)):
        if idx + 1 < len(plans):
            currTask, nextTask = plans[idx], plans[idx+1]
            
            #시간을 찾음
            currEndTime = currTask[1] + currTask[2]#진행 중 과제 종료시간
            nextStartTime = nextTask[1]#다음과제 시작시간
            
            #다음 과제 시작시간이 현재 진행 중인 프로세스 종료시간보다 빠른 경우
            if nextStartTime < currEndTime:
                #현재과제의 걸리는 시간을 업데이트
                currTask[2] -= nextStartTime - currTask[1]
                stack.append(currTask)
            else:
                #현재 작업을 완료시킴
                result.append(currTask[0])
                
                diffTime = nextStartTime - currEndTime
                while stack:
                    #멈춘과제에서 하나를 꺼내와 현재 과제로 설정
                    currTask = stack.pop()
                    
                    if diffTime >= currTask[2]:
                        result.append(currTask[0])
                        diffTime -= currTask[2]
                    else:
                        currTask[2] -= diffTime
                        stack.append(currTask)
                        break
    stack.append(plans[-1])        
    while stack:
        result.append(stack.pop()[0])
    return result
                
            