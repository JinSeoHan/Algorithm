import heapq
def solution(fees, records):
    infoL = dict()
    result = dict()
    for i, record in enumerate(records):
        time, number, cmd = record.split()
        
        if cmd == 'IN':
            infoL[number] = time
        else:
            total = getTimeMin(infoL[number], time)
            if number not in result:
                result[number] = total
            else:
                result[number] += total
            del(infoL[number])
    for k, v in infoL.items():
        time = getTimeMin(v, None)
        if k not in result: result[k] = time
        else: result[k] += time
    l = []
    for k, v in result.items():
        l.append((k, getFee(fees, v)))
    l.sort()
    result = []
    for i in l:
        result.append(i[1])
        
    return result
        
def getFee(fees, time):
    defTime, defFee, unitTime, unitFee = tuple(fees)
    
    if time >= defTime:
        v1 = (time-defTime)/unitTime
       	v2 = (time-defTime)//unitTime
        if v1 - v2 != 0:
            fee = (v2+1) * unitFee
        else: fee = v2 * unitFee
        return defFee + fee
    else:
        return defFee
        
def getTimeMin(sTime, eTime):
    totalTime = 0
    if eTime == None:
        eTime = '23:59'
    eh, em = map(int, eTime.split(':'))
    sh, sm = map(int, sTime.split(':'))
    if sh == eh:
        totalTime = em - sm
    else:
        if sm <= em:
            totalTime += em - sm
            totalTime += 60 * (eh - sh)
        else:
            totalTime += 60 -sm + em
            totalTime += 60 * (eh - sh - 1)
            
    return totalTime
    