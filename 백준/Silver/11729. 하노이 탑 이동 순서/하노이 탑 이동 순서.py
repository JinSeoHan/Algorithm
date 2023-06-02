import sys
input = sys.stdin.readline

ruleL = [1,2,3]
def hanoi(num):
    if num == 1:
        return [(1,3)]  
    #이전 하노이 결과 찾음
    prevHanoiL = hanoi(num-1)
    #홀짝 결정
    rule = 1
    if num % 2 != 0:
        rule = -1

    ruleIdx = 0
    result = []
    for e in prevHanoiL:
        result.append((ruleL[ruleIdx], ruleL[(ruleIdx + rule) % 3]))
        result.append(e)
        ruleIdx = (ruleIdx + rule) % 3
    result.append((ruleL[ruleIdx], ruleL[(ruleIdx + rule) % 3]))
    return result

n = int(input())

l = hanoi(n)
print(len(l))
for i in l:
    print(i[0], i[1])