def solution(rows, columns, queries):
    matrix = [[row*columns+column for column in range(1, columns+1)] for row in range(rows)]
    result = []
    for q in queries:
        si, sj, ei, ej = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        
        ci, cj = si, sj
        currV = matrix[ci][cj]
        prevV = currV
        
        #위
        result.append(currV)
        while cj <= ej:
            currV = matrix[ci][cj]
            result[-1] = min(result[-1], currV)
            matrix[ci][cj] = prevV
            prevV = currV
            cj += 1
            
        #오
        ci, cj = ci+1, cj-1
        while ci <= ei:
            currV = matrix[ci][cj]
            result[-1] = min(result[-1], currV)
            matrix[ci][cj] = prevV
            prevV = currV
            ci += 1
        #아
        ci, cj = ci-1, cj-1
        while sj <= cj:
            currV = matrix[ci][cj]
            result[-1] = min(result[-1], currV)
            matrix[ci][cj] = prevV
            prevV = currV
            cj -= 1
        #왼
        ci, cj = ci-1, cj+1
        while si <= ci:
            currV = matrix[ci][cj]
            result[-1] = min(result[-1], currV)
            matrix[ci][cj] = prevV
            prevV = currV
            ci -= 1
    return result
            
            
            
            
            
            
        
        
        