def solution(n, words):
    ord, count = 0, 0
    cnt = [[] for i in range(n)]
    cnt[0].append(words[0])
    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1] and words[i] not in words[:i]:
            cnt[i%(n)].append(words[i])
        else:
            ord = i%(n) + 1
            count = len(cnt[i%n]) + 1
            break
    return [ord, count]