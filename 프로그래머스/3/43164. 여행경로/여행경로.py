def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    return sol2(["ICN"], len(tickets) ,tickets)
def sol2(ord, length ,tickets):
    if len(ord) == length + 1: 
        return ord
    
    result = 0
    for i, value in enumerate(tickets):
        if ord[-1] == value[0]:
            newTick = tickets.copy()
            del newTick[i]
            result = sol2(ord+[value[1]], length, newTick)
            if result: return result