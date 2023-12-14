'''
(()[[]])
다음과 같은 순서로 저장됨
(, []

(, []
(, []

(, [2]

[, []
(, [2]

[, []
[, []
(, [2]

[, [3] #1*3
(, [2]

( [2, 9] 

( [2, 9] #(2+9)*2
result = [22]
'''
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

#입력받음
v = input().rstrip()

pair = defaultdict(str)
pair[')'] = '('
pair[']'] = '['

queue = deque(v) #입력값 큐 저장
result = [] #올바른 괄호열 결과를 저장
stack = [] #중첩된 올바른 괄호열 계산을 위한 스택
while queue:
    curr = queue.popleft()
    #열린괄호 저장
    if curr == '(' or curr == '[':
        stack.append([curr, []])

    #예외처리
    if curr == ')' or curr == ']':
        #닫힌 괄호 중 스택이 비어있거나 짝매칭이 안되면 종료
        if not stack or stack[-1][0] != pair[curr]:
            result = [0]
            break
        #괄호, 더해야할 값리스트
        v, tmp = stack.pop()
        s = sum(tmp)
        s = 1 if not s else s #더할 값이 없으면 1 있으면 합 반환
        opResult = s*2 if v == '(' else s*3#유형에 맞는 곱연산

        #스택이 비어있다면 root 괄호결과
        if not stack:
            result.append(opResult)
        #비어있지않다면 부모스택에 값 저장
        else:
            stack[-1][1].append(opResult)

print(sum(result))