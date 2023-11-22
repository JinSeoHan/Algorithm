def isCorrect(v):
    stack = []
    for i in v:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
    return not stack
def solution(p):
    if isCorrect(p) or len(p) == 0: 
        return p
    #u, v 분리
    cnt1, cnt2 = 0, 0
    idx = 0
    for i in range(len(p)):
        if p[i] == '(': cnt1 += 1
        else: cnt2 += 1
        if cnt1 == cnt2: 
            idx = i
            break
    u = p[:idx+1]
    v = p[idx+1:]
    #u가 올바른 괄호 문자열인 경우
    if isCorrect(u):
        v = u + solution(v) 
        return v
    #u가 올바른 괄호 문자열이 아닌경우
    else:
        u = list(u[1:len(u)-1])
        for i, value in enumerate(u):
            if value == '(':
                u[i] = ')'
            else:
                u[i] = '('
        u = ''.join(u)
        v = '(' + solution(v) + ')' + u
        return v