quacks = list(input())
w = 'kcauq'
result = 0
idx = 0
while quacks.count(0) != len(quacks):
    isCorrect = False
    for i in range(len(quacks)-1, -1, -1):
        # 녹음한 소리가 옳은지
        if quacks[i] == w[(idx%5)]:
            if idx%5 == 4:
                isCorrect = True
            quacks[i] = 0
            if idx%5 == 0:
                isCorrect = False
            idx += 1
    result += 1
    if not isCorrect:
        result = -1
        break
print(result)