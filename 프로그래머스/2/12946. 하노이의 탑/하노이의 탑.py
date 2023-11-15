result = []
def recur(n, n1, n2, n3):
    global result
    if n == 1:
        result.append([n1, n3])
        return
    recur(n-1, n1, n3, n2)
    result.append([n1, n3])
    recur(n-1, n2, n1, n3)
    
def solution(n):
    recur(n, 1, 2, 3)
    return result
    
    
    