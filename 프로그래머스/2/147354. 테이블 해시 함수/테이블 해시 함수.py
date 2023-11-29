def getS_i(data, i):
    result = 0
    for v in data[i]:
        result += v % (i+1)
    return result
        
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col-1], -x[0]))
    result = 0
    for i in range(row_begin-1, row_end):
        result ^= getS_i(data, i)
    return result
    
