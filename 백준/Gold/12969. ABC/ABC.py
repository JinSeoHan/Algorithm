'''
힌트 : 출근기록 문제와 유사하게 접근

abc(wCnt, a, b, pCnt) : '단어수', 'a개수', 'b개수', '쌍의 개수'

<쌍의 개수>
case 1 : A가 붙는 경우
(ABCDA...)A => A가 붙기전 문자열에서 어떤 수가 나오더라도 쌍을 만들 수 없음 따라서 0
case 2 : B가 붙는 경우
(ABCDA...)B => B가 붙기전 문자열(ABCDA...)의 A의 개수
case 3 : C가 붙는 경우
(ABCDA...)C => C가 붙기전 문자열(ABCDA...)의 A와 B의 개수

abc(wCnt, a, b, pCnt) 에서 c의 개수를 넣지 않는이유 => wCnt-a-b가 c개수라는 뜻을 내포하고 있어 생략
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [[[[False]*500 for b in range(30)] for a in range(30)] for wcnt in range(n)]
result = ['']*n
def abc(wCnt, a, b, pCnt):
    if wCnt == n:
        if pCnt == k:
            print(''.join(result))
            exit(0)
        return
    if visited[wCnt][a][b][pCnt]: return
    visited[wCnt][a][b][pCnt] = True
    result[wCnt] = 'A'
    abc(wCnt+1, a+1, b, pCnt)
    result[wCnt] = 'B'
    abc(wCnt+1, a, b+1, pCnt+a)
    result[wCnt] = 'C'
    abc(wCnt+1, a, b, pCnt+a+b)

abc(0,0,0,0)
print(-1)