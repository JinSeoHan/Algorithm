def solution(s):
    answer = ''
    lower = s.lower()
    for i in range(len(s)):
        if 'a' <= lower[i] <= 'z':
            if lower[i-1] == ' ' or i == 0:
                answer += lower[i].upper()
                continue
        answer += lower[i]
    return answer