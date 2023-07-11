import sys
from collections import Counter
input = sys.stdin.readline

input()
count = Counter(map(int,input().split()))
input()
for i in map(int,input().split()):
    print(count[i], end=" ") if i in count else print(0, end=" ")