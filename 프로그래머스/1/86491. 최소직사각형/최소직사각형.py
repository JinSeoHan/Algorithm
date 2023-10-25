def solution(sizes):
    ga = []
    se = []
    for i in sizes:
        a, b = i[0], i[1]
        if a > b:
            ga.append(a)
            se.append(b)
        else:
            ga.append(b)
            se.append(a)
    gaM, seM = max(ga), max(se)
    return gaM * seM