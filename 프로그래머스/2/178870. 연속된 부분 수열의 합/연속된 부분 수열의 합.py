def solution(sequence, k):
    
    #start, end
    s,e = 0, 0
    #연속된 수열의 합
    sum = 0
    #k가 만들어진 수열의 인덱스 범위 리스트
    result = []
    
    while True:
        if sum == k:
            result.append([s,e-1])
            sum -= sequence[s]
            s += 1
        elif sum < k:
            #범위를 벗어나지 못하게 처리
            if e == len(sequence): break
            sum += sequence[e]
            e += 1
        elif sum > k:
            sum -= sequence[s]
            s += 1
    #print('before', result)
    result.sort(key=lambda x : abs(x[0]-x[1]))
    #print('after', result)
    return result[0]