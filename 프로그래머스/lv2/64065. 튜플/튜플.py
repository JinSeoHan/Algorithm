def solution(s):
    answer = []
    s = s.replace('}}','}')
    s = s.replace('{{','{')
    s = s.replace('{','')
    tokens = s.split('}')
    tokens.remove('')
    
    for token in tokens:
        if ',' in token:
            token = token.split(',')
            if '' in token:
                token.remove('')
            
            answer.append(list(map(int, token)))
        else:
            token = int(token)
            answer.append([token])
    answer.sort(key=lambda a : len(a))
    s = set()
    result = []
    for l in answer:
        for i in l:
            if i not in s:
                s.add(i)
                result.append(i)
    return result