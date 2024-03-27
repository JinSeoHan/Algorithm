from collections import defaultdict
import sys
input = sys.stdin.readline


def removeTopRanker(dicList):
    topRankCnt = dicList[-1][1]
    while dicList and topRankCnt == dicList[-1][1]:
        dicList.pop()
    return dicList
def extractTop2Rankers(dicList):
    top2RankCnt = dicList[-1][1]
    top2List = []
    while  dicList and top2RankCnt == dicList[-1][1]:
        top2List.append(dicList[-1][0])
        dicList.pop()
    top2List.sort()
    return top2List


while (v := tuple(map(int, input().split()))) != (0,0):
    dic = defaultdict(int)
    n, m = v[0], v[1]

    # 랭킹에 들어선 횟수 저장
    for _ in range(n):
        for v in map(int, input().split()):
            dic[v] += 1
    dicList = list(dic.items()) 
    dicList.sort(key=lambda x : x[1])
    
    # 랭킹 1위 제거
    dicList = removeTopRanker(dicList)
    # 랭킹 2위 추출 및 정렬
    top2List = extractTop2Rankers(dicList)
    # 랭킹 2위 출력
    print(*top2List)