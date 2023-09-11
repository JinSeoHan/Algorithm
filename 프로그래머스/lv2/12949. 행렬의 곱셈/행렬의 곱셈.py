def solution(arr1, arr2):
    result = [[] for r in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            s = 0
            for k in range(len(arr1[0])):
                s += arr1[i][k] * arr2[k][j]
            result[i].append(s)
    return result