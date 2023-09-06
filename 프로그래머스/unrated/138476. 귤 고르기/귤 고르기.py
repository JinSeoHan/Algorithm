def solution(k, tangerine):
    list = []
    count = dict()
    for i in tangerine:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1
    for key, value in count.items():
        list.append((value, key))
    list.sort(reverse=True)
    result = 0
    cnt = 0
    for value, key in list:
        result += value
        cnt += 1
        if result >= k:
            break;
    return cnt
