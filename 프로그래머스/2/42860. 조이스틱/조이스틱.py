from collections import deque

def change(currName, name, idx):
    currV = ord(currName[idx])
    originV = ord(name[idx])
    currName = currName[:idx] + name[idx] + currName[idx+1:]
    
    diff = abs(currV-originV)
    return min(diff, 26-diff), currName
    
def solution(name):
    initstr = ''.join(['A']*len(name))
    #커서의 위치
    idx = 0
    queue = deque()
    #현재커서, 현재수정이름, 수정횟수
    queue.append((idx, initstr, 0, 0))
    
    result = 1000000000
    while queue:
        currIdx, currName, currCnt, chrCnt = queue.popleft()
        if chrCnt == len(name) or currName == name:
            if currName == name:
                result = min(result,currCnt)
            continue
        
        #현재 커서값이 변경해야할 이름과 다른경우
        if currName[currIdx] != name[currIdx]:
            changeCnt, nextName = change(currName, name, currIdx)
            queue.append((currIdx, nextName, currCnt + changeCnt, chrCnt + 1))
        #현재 커서값이 변경해야할 이름과 같은경우 커서이동
        else:
            #오른쪽으로 이동 A찾음
            rCnt = 0
            for i in range(currIdx+1, currIdx + len(name)):
                rCnt += 1
                if currName[i%len(name)] == 'A' and currName[i%len(name)] != name[i%len(name)]:
                    rpos = i%len(name)
                    break
            #왼쪽으로 이동 A찾음
            lCnt = 0
            for i in range(currIdx-1, currIdx-len(name) , -1):
                lCnt += 1
                if currName[abs(i+len(name))%len(name)] == 'A' and currName[abs(i+len(name))%len(name)] != name[abs(i+len(name))%len(name)]:
                    lpos = abs(i+len(name))%len(name)
                    break
            
            #작은쪽으로이동
            queue.append((lpos, currName, currCnt+lCnt, chrCnt))
            queue.append((rpos, currName, currCnt+rCnt, chrCnt))
    return result