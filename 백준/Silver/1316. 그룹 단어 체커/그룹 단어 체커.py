def isGroupWord(word):

    prev = word[0]
    s = set()
    for i in range(len(word)):
        if (word[i] not in s) or prev == word[i]:
            prev = word[i]
            s.add(word[i])
        else:
            return False

    return True

result = 0
for _ in range(int(input())):
    word = input()
    if isGroupWord(word): result += 1
print(result)