n = int(input())

s = set()
for _ in range(n):
    orgWords = input()
    # orgWordsList = list(orgWords) # 한글자씩 들어가있는 list
    words = list(map(list, orgWords.split()))
    # 단어의 첫 글자 검증
    flag1 = False
    for word in words:
        if word[0] in s: continue

        s.add(word[0].upper())
        s.add(word[0].lower())
        word.insert(0, '[')
        word.insert(2, ']')
        # 출력
        temp = []
        for v in words:
            temp.append(''.join(v))
        print(' '.join(temp))
        flag1 = True
        break
    if flag1: continue
    # 순차적으로 검증
    flag2 = False
    for i, c in enumerate(orgWords):
        if c in s or c == ' ': continue

        s.add(c.upper())
        s.add(c.lower())
        print(orgWords[:i] + '[' + c + ']' + orgWords[i+1:])
        flag2 = True
        break
    if flag2: continue
    print(orgWords)