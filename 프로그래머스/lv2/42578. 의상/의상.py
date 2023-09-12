from itertools import combinations
clothDict = dict()
def solution(clothes):
    for name, kind in clothes:
        if kind not in clothDict:
            clothDict[kind] = 1
        else:
            clothDict[kind] += 1
    result = 1
    for key in clothDict.keys():
        result *= clothDict[key] + 1
    return result -1