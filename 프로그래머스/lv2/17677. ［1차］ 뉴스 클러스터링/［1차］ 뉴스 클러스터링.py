def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dictStr1 = {}
    dictStr2 = {}
    #다중집합 원소로 만들기 로직
    for i in range(len(str1)-1):
        flag = False
        for v in str1[i:i+2]:
            if not (ord('a') <= ord(v) <= ord('z')): flag = True
        if not flag:
            if str1[i:i+2] not in dictStr1:
                dictStr1[str1[i:i+2]] = 1
            else:
                dictStr1[str1[i:i+2]] += 1
                         
    for i in range(len(str2)-1):
        flag = False
        for v in str2[i:i+2]:
            if not (ord('a') <= ord(v) <= ord('z')): flag = True
        if not flag:
            if str2[i:i+2] not in dictStr2:
                dictStr2[str2[i:i+2]] = 1
            else:
                dictStr2[str2[i:i+2]] += 1
    #합집합 교집합 찾기
    unionCnt, interCnt = 0, 0
    for key, value in dictStr1.items():
        if key in dictStr2:
            interCnt += min(value, dictStr2[key])
            unionCnt += max(value, dictStr2[key])
            continue
        unionCnt += value
    for key, value in dictStr2.items():
        if key not in dictStr1:
            unionCnt += value

    return 65536 if unionCnt == 0 else int(interCnt/unionCnt*65536)