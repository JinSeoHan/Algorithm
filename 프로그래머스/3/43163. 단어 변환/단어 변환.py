def solution(begin, target, words):
    if target not in words: return 0
    return DFS(begin, target, words, 0)
        
def DFS(cWord, target, words, cnt):
    if cWord == target:
        return cnt
    for i, nWord in enumerate(words):
        if not isOneDiff(cWord, nWord): continue
        if len(words) != 1:
            del words[i]
            v = DFS(nWord, target, words, cnt+1)
            words.insert(i, nWord)
            if v : return v
    return 0
def isOneDiff(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    return cnt == 1