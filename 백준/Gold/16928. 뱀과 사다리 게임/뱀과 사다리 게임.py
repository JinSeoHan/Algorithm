import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
def BFS():
    queue.append(1)
    while queue:
        currLoc = queue.popleft()
        for num in range(1, 7):
            nLoc = currLoc + num
            if nLoc <= 100:
                if board[nLoc] == 0:
                    if nLoc not in ladderDest.keys() and nLoc not in snakeDest.keys():
                        queue.append(nLoc)
                    board[nLoc] = board[currLoc] + 1
                elif board[nLoc] > board[currLoc] + 1:
                        board[nLoc] = board[currLoc] + 1
                        queue.append(currLoc)
            
                if nLoc in ladderDest.keys():
                    nnLoc = ladderDest[nLoc]
                    if board[nnLoc] == 0:
                        queue.append(nnLoc)
                        board[nnLoc] = board[nLoc]
                    elif board[nnLoc] > board[nLoc]:
                        queue.append(nnLoc)
                        board[nnLoc] = board[nLoc]
                elif nLoc in snakeDest.keys():
                    nnLoc = snakeDest[nLoc]
                    if board[nnLoc] == 0:
                        queue.append(nnLoc)
                        board[nnLoc] = board[nLoc]
                    elif board[nnLoc] > board[nLoc]:
                        queue.append(nnLoc)
                        board[nnLoc] = board[nLoc]

N, M = map(int, input().split())
board = [0] * 101

ladderDest = dict()
for n in range(N):
    x, y = map(int, input().split())
    ladderDest[x] = y

snakeDest = dict()
for m in range(M):
    u, v = map(int, input().split()) 
    snakeDest[u] = v

BFS()

print(board[100])