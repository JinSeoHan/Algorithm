def solution(s):
    convCnt, zeroCnt = 0, 0
    while s != '1':
        zeroCnt += s.count('0')
        s = str(bin(len(s.replace('0', '')))[2:])
        convCnt += 1
    return [convCnt, zeroCnt]