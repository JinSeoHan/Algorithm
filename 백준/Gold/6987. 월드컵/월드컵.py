'''
bottom-up방식으로는 가지치기가 안된다. 근데 가지치기를 하고싶다 -> 소거법으로 생각
'''
from itertools import combinations
import sys
input = sys.stdin.readline

def dfs(round):
    if round == 15:
        for w,d,l in board:
            if (w,d,l) != (0,0,0): 
                return False
        return True

    result = False
    t1, t2 = games[round]

    # 승 패
    if board[t1][0] > 0 and board[t2][2] > 0:
        board[t1][0] -= 1
        board[t2][2] -= 1
        result = dfs(round+1)
        board[t1][0] += 1
        board[t2][2] += 1
    # 무 무 
    if board[t1][1] > 0 and board[t2][1] > 0 and not result:
        board[t1][1] -= 1
        board[t2][1] -= 1
        result = dfs(round+1)
        board[t1][1] += 1
        board[t2][1] += 1
    # 패 승
    if board[t1][2] > 0 and board[t2][0] > 0 and not result:
        board[t1][2] -= 1
        board[t2][0] -= 1
        result = dfs(round+1)
        board[t1][2] += 1
        board[t2][0] += 1
    return result

#대전표
games = list(combinations(range(6), 2))

result = []
for _ in range(4):
    temp = list(map(int, input().split()))
    board = [temp[i:i+3] for i in range(0, 16, 3)]
    result.append(1 if dfs(0) else 0)

for i in result:
    print(i, end=' ')