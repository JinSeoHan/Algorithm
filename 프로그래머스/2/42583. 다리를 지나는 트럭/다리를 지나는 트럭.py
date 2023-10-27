from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for i in range(bridge_length)])
    cWeight = 0 #현재무게
    time = 0 #경과시간
    
    for truck_weight in truck_weights:
        #다리 무게가 가벼워질때까지 기다리는 시간
        while not (cWeight + truck_weight - bridge[0] <= weight):
            #다리에 입장
            bridge.append(0)
            #다리 통과
            passTruck = bridge.popleft()
            cWeight -= passTruck
            #시간 경과
            time += 1
            
        #다리에 입장
        bridge.append(truck_weight)
        cWeight += truck_weight
        #다리 통과
        passTruck = bridge.popleft()
        cWeight -= passTruck
        #시간 경과
        time += 1
    #다리에 남아있는 트럭이 빠져나가는 시간
    while cWeight != 0:
        #다리에 입장
        bridge.append(0)
        #다리 통과
        passTruck = bridge.popleft()
        cWeight -= passTruck
        #시간 경과
        time += 1
    return time