import sys
sys.setrecursionlimit(10**9)
def solution(word):
    dfs('', word)
    return cnt

cnt = 0
def dfs(curr, word):
    global cnt
    if len(curr) == 5:
        if curr == word: return True
        else: return False
    
    if curr == word: return True
    for v in ['A', 'E', 'I', 'O', 'U']:
        curr += v
        cnt += 1
        if dfs(curr, word): return True
        curr = curr[:-1]
    return False