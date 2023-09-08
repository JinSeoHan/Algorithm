#def solution(n, left, right):
#    result = []
#    cnt = -1
#    flag = False
#    for i in range(n):
#        for j in range(i):
#            cnt += 1
#            if left <= cnt <= right:
#                result.append(i+1)
#            if right < cnt: 
#                flag = True
#                break
#        for j in range(i, n):
#            cnt += 1
#            if left <= cnt <= right:
#                result.append(j+1)
#            if right < cnt: 
#                flag = True
#                break
#        if flag: break
#    return result
def solution(n, left, right):
    flag = False
    result = []
    sr = left//n
    er = right//n
    cnt = sr*n-1
    for i in range(sr, er+1):
        for j in range(i):
            cnt += 1
            if left <= cnt <= right:
                result.append(i+1)
            if right < cnt: 
                flag = True
                break
        for j in range(i, n):
            cnt += 1
            if left <= cnt <= right:
                result.append(j+1)
            if right < cnt: 
                flag = True
                break
        if flag: break
    return result
