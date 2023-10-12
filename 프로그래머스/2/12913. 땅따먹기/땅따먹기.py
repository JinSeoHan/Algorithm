def solution(land):
    for i in range(len(land)):
        if i == 0 : continue
        for j in range(4):
            m = 0
            for k in range(4):
                if j == k: continue
                m = max(m, land[i-1][k])
            land[i][j] += m
    return max(land[-1])
