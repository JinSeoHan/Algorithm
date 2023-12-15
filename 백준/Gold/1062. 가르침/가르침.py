from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())


words = []
#anti tica 사이의 문자를 이어붙임
teach = ['a','n','t','i','c']
for _ in range(n):
    s = input()
    words.append(s[4:len(s)-4])
#기본학습단어 조차 가르치지 못한 경우 종료
if k < 5: 
    print(0)
    exit(0)

s = list('bdefghjklmopqrsuvwxyz')

result = 0
for combi in combinations(s, k-5):
    tmp = teach.copy()
    for c in combi:
        tmp.append(c)
    
    #해당 단어가 배운 글자로만 이루어져있는지
    cnt = 0
    for word in words:
        flag = True
        for c in word:
            if c not in tmp: 
                flag = False
                break
        if flag: cnt += 1
            
    result = max(result, cnt)
print(result)