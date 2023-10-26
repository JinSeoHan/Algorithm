mv = None
def solution(begin, target, words):
    global mv
    mv = len(words)
    if target not in words: return 0
    DFS(begin, target, words, 0)
    return mv
        
def DFS(cWord, target, words, cnt):
    global mv
    if cWord == target:
        mv = min(mv, cnt)
        return cnt
    for i, nWord in enumerate(words):
        if not isOneDiff(cWord, nWord): continue
        if len(words) != 1:
            del words[i]
            v = DFS(nWord, target, words, cnt+1)
            words.insert(i, nWord)
    return 0
def isOneDiff(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    return cnt == 1