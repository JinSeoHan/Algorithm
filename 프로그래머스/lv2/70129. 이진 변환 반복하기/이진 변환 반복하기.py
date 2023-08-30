zeroCnt = 0
def deleteZero(s):
    global zeroCnt
    for i in s:
        if i == '0': zeroCnt += 1
    return s.replace('0', '')
def solution(s):
    convCnt = 0
    while s != '1':
        s = deleteZero(s)
        length = len(s)
        s = str(bin(length)[2:])
        convCnt += 1
    return [convCnt, zeroCnt]