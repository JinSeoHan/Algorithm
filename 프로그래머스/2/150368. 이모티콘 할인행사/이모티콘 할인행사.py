from itertools import permutations, product
def solution(users, emoticons):
    result = []
    l = [0.1, 0.2, 0.3, 0.4]
    rates = []
    #이모티콘 개수만큼 비율을 넣음
    for i in range(len(emoticons)):
        rates.append(l)
    # 모든 비율rate == [10,10,10,10]
    for rate in product(*rates) :
        #모든 유저의 가입여부를 찾음
        temp = [0, 0]
        for user in users:
            sum = 0
            for i, r in enumerate(rate):
                if user[0] <= r*100:
                    sum += emoticons[i]*(1-r)
            # 구매비용이 사용자가 생각하는 가격보다 큰 경우 플러스가입
            if sum >= user[1]:
                temp[0] += 1
            else:
                temp[1] += int(sum)
        result.append(temp)
    result.sort(key=lambda x : (x[0], x[1]))
    return result[-1]