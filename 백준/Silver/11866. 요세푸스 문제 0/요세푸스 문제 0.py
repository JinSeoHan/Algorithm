import sys
from collections import deque
input = sys.stdin.readline

n ,k = map(int, input().split())
queue = deque()
resultList = []
for i in range(1, n + 1):
    queue.append(str(i))

index = 0
while queue:
    index += k - 1
    while index > n - 1:
        index -= n
    resultList.append(queue[index])
    del queue[index]
    n -= 1
    
str1 = ', '.join(resultList)
print('<' + str1 + '>')